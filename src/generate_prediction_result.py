from datetime import datetime, timedelta, time
import pandas as pd
from loguru import logger
import glob
from pathlib import Path
from utils import calculate_matches
from vietlott.config.products import get_config

top_counter = 60

class PredictionAnalyzer:
  def _load_lottery_data(self, product: str) -> pd.DataFrame:
    """Load and prepare lottery data for analysis."""
    try:
      df = pd.read_json(get_config(product).raw_path, lines=True, dtype=object, convert_dates=False)
      df["date"] = pd.to_datetime(df["date"])
      # For power535, keep the time. For others, just use the date.
      if product != 'power535':
          df["date"] = df["date"].dt.date
      df = df.sort_values(by=["date", "id"], ascending=False)
      return df
    except Exception as e:
      logger.error(f"Error loading data for {product}: {e}")
      return pd.DataFrame()    
  
  def _compare_predictions_with_results(self, product_name: str, df_hist: pd.DataFrame):
    """Compares prediction files with historical results and saves the outcome."""
    prediction_files = glob.glob(f'./data/prediction/{product_name}*.jsonl')
    
    # Prepare historical data for efficient lookup.
    # For power535, the key includes time. For others, it's just the date.
    hist_map = {}
    if product_name == 'power535':
      df_hist_asc = df_hist.sort_values(by=["date", "id"], ascending=True)
      for index, row in df_hist_asc.iterrows():
        key = row['date'].strftime('%Y-%m-%d 21:%M')
        if (index % 2 == 0):
          key = row['date'].strftime('%Y-%m-%d 13:%M')
        hist_map[key] = row['result']
    else:
      for _, row in df_hist.iterrows():
        key = row['date'].strftime('%Y-%m-%d')
        hist_map[key] = row['result']

    for pred_file_path in prediction_files:
        if '_result' in pred_file_path:
            continue # Skip already processed files
        try:
            df_pred = pd.read_json(pred_file_path, lines=True, convert_dates=False)
            df_pred['date'] = pd.to_datetime(df_pred['date'])
            if df_pred.empty:
                continue

            results = []
            for _, pred_row in df_pred.iterrows():
              if product_name == 'power535':
                  pred_date_str = pred_row['date'].strftime('%Y-%m-%d %H:%M')
              else:
                  pred_date_str = pred_row['date'].strftime('%Y-%m-%d')
              actual_result = hist_map.get(pred_date_str)
              
              result = {
                'date': pred_date_str,
                'result': pred_row['result']
              }
              if ("_prediction" in pred_file_path):
                result['strategy'] = pred_row['strategy']
              elif ("_hot" in pred_file_path ):
                result['strategy'] = "HotNumbers"
              elif ("_cold" in pred_file_path):
                result['strategy'] = "ColdNumbers"
              else:
                result['strategy'] = "Unknown"
              
              if actual_result:
                  is_special_product = product_name in ["power655", "power535"]
                  
                  match_info = calculate_matches(pred_row['result'], actual_result, is_special_product)
                  result['matches_count'] = match_info['matches_count']
                  result['matches_result'] = match_info['matches_result']
                  if is_special_product:
                    result['matches_special_number'] = match_info.get('matches_special_number', False)
              else:
                  result['matches_count'] = "Waiting"
                  result['matches_result'] = "Waiting"
                  if (product_name == "power655" or product_name == "power535"):
                    result['matches_special_number'] = "Waiting"
              results.append(result)

            df_results = pd.DataFrame(results)
            # Create a 'result' subdirectory if it doesn't exist
            result_dir = Path(pred_file_path).parent / "result"
            result_dir.mkdir(exist_ok=True)
            output_path = result_dir / f"{Path(pred_file_path).stem}_result.jsonl"
            df_results.to_json(output_path, orient="records", lines=True, date_format="iso")
            logger.info(f"Saved comparison results to {output_path}")
        except Exception as e:
            logger.error(f"Failed to process prediction file {pred_file_path}: {e}")
            
  def _analyze_strategy_performance(self, product_name: str):
      """Analyzes and aggregates the performance of different prediction strategies."""
      result_files = glob.glob(f'./data/prediction/result/{product_name}*_result.jsonl')
      if not result_files:
          logger.warning(f"No result files found for {product_name} to analyze strategy performance.")
          return

      all_results_df = pd.concat([pd.read_json(f, lines=True) for f in result_files], ignore_index=True)

      # Filter out entries that are still waiting for results
      valid_results_df = all_results_df[all_results_df['matches_count'] != 'Waiting'].copy()
      valid_results_df['matches_count'] = pd.to_numeric(valid_results_df['matches_count'])

      if valid_results_df.empty:
          logger.info(f"No completed results to analyze for {product_name}.")
          return

      # Group by strategy and then by matches_count
      strategy_summary = valid_results_df.groupby(['strategy', 'matches_count']).size().reset_index(name='count')
      
      # Pivot the table to have strategies as rows and match counts as columns
      performance_summary = strategy_summary.pivot_table(
          index='strategy', 
          columns='matches_count', 
          values='count', 
          fill_value=0
      )

      # Calculate total analyzed tickets for each strategy
      performance_summary['total_analyzed'] = performance_summary.sum(axis=1)

      # If 'matches_special_number' exists, calculate its stats
      if 'matches_special_number' in valid_results_df.columns:
          special_matches_df = valid_results_df[valid_results_df['matches_special_number'] == True]
          if not special_matches_df.empty:
              special_summary = special_matches_df.groupby('strategy').size().reset_index(name='special_number_wins')
              # Merge this into the main performance summary
              performance_summary = performance_summary.merge(special_summary, on='strategy', how='left').fillna(0)

      # After pivoting and merging, the 'strategy' column might be part of the index.
      # Let's reset it to ensure we can safely convert other columns to numeric types.
      if 'strategy' in performance_summary.index.names:
          performance_summary = performance_summary.reset_index()

      # Calculate radius (percentage) for each match count
      match_cols = [col for col in performance_summary.columns if col not in ['strategy', 'total_analyzed']]
      for col in match_cols:
          radius_col_name = f"{col}_radius"
          performance_summary[radius_col_name] = (performance_summary[col] / performance_summary['total_analyzed'] * 100).round(2)
      
      # Save the summary to a file
      summary_output_path = Path(f'./data/prediction/result/{product_name}_strategy_summary.json')
      performance_summary.reset_index().to_json(summary_output_path, orient='records', indent=4)
      logger.info(f"Saved strategy performance summary for {product_name} to {summary_output_path}")

  def _analyze_duplicated_tickets(self, product_name: str):
      """Analyzes duplicated tickets across all prediction result files."""
      result_files = glob.glob(f'./data/prediction/result/{product_name}*_result.jsonl')
      if not result_files:
          logger.warning(f"No result files found for {product_name} to analyze for duplicates.")
          return

      all_results_df = pd.concat([pd.read_json(f, lines=True) for f in result_files], ignore_index=True)

      if all_results_df.empty:
          logger.info(f"No results to analyze for duplicates in {product_name}.")
          return

      # Convert list to a hashable type (sorted tuple) to find duplicates
      all_results_df['ticket_tuple'] = all_results_df['result'].apply(lambda x: tuple(sorted(x)))

      # Find duplicated tickets
      duplicates_df = all_results_df[all_results_df.duplicated(subset=['ticket_tuple'], keep=False)].copy()

      if duplicates_df.empty:
          logger.info(f"No duplicated tickets found for {product_name}.")
          return

      logger.info(f"Found {len(duplicates_df['ticket_tuple'].unique())} duplicated tickets for {product_name}.")

      # Group by ticket to see which strategies and dates generated it
      duplicates_summary = duplicates_df.groupby('ticket_tuple').agg(
          count=('strategy', 'size'),
          strategies=('strategy', lambda x: sorted(list(x.unique()))),
          dates=('date', lambda x: sorted(list(x.unique())))
      ).reset_index().sort_values('count', ascending=False)

      # Save the summary to a file
      summary_output_path = Path(f'./data/prediction/result/{product_name}_duplicated_tickets_summary.jsonl')
      duplicates_summary.to_json(summary_output_path, orient='records', lines=True)
      logger.info(f"Saved duplicated tickets summary for {product_name} to {summary_output_path}")

  def generate(self) -> str:
    """Generate the complete prediction content."""
    logger.info("Starting Prediction generation...")

    # Load Power 6/55 data (main focus)
    df_power655 = self._load_lottery_data("power_655")
    
    # Load Power 6/45 data (main focus)
    df_power645 = self._load_lottery_data("power_645")
    
    # Load Power 5/35 data (main focus)
    df_power535 = self._load_lottery_data("power_535")
    
    # Compare predictions with results
    self._compare_predictions_with_results("power655", df_power655)
    self._compare_predictions_with_results("power645", df_power645)
    self._compare_predictions_with_results("power535", df_power535)

    # Analyze strategy performance
    self._analyze_strategy_performance("power655")
    self._analyze_strategy_performance("power645")
    self._analyze_strategy_performance("power535")

    # Analyze duplicated tickets
    self._analyze_duplicated_tickets("power655")
    self._analyze_duplicated_tickets("power645")
    self._analyze_duplicated_tickets("power535")
    
    return "Prediction analyzer finished."
    
def main():
    """Main entry point for analytic analyzer."""
    try:
        generator = PredictionAnalyzer()
        generator.generate()
        logger.info("Prediction analyzer completed successfully!")
    except Exception as e:
        logger.error(f"Failed to analyzer prediction: {e}")
        raise


if __name__ == "__main__":
    main()