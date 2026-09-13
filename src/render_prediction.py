#!/usr/bin/env python
# Author: Cong Pham <chicong7891@gmail.com>
"""
Script showing how to use the lottery prediction strategies.

source .venv/bin/activate
"""
from machine_learning.strategies.pair_frequency import PairFrequencyStrategy
import pandas as pd
from datetime import datetime
from loguru import logger
import argparse
import polars as pl
from vietlott.config.productsV2 import get_config
from machine_learning.strategies import RandomModel, PatternStrategy
from utils import analyze_odd_even_counter, get_next_draw_date, save_predictions

def main(product: str, number: int = 10):
    """Run all demonstrations."""
    logger.info(f"🎰 Vietlott Strategy Demo Starting...")
    try:
        config = get_config(product)
        logger.debug(f"Loaded configuration for {product}: {config}")
        df_pl = pl.read_ndjson(config.raw_path)
        df_pl = df_pl.with_columns(pl.col("date").str.to_date(strict=False))
        df_pd = df_pl.to_pandas()

        next_draw_date_str = get_next_draw_date({
            "days_of_week": config.days_of_week,
            "time_range": config.time_range,
            "time": config.time,
        })
        next_draw_date = pd.Timestamp(next_draw_date_str) 
        logger.info(f"Next draw date for {product} is: {next_draw_date}")
        
        prediction_records = []
        time_predict = 5  # Number of predictions to generate for each strategy
        # Random Strategy
        random_model = RandomModel(df_pd, time_predict=time_predict, min_val=config.min_value, max_val=config.max_value)
        random_model.number_predict = config.size_output
        random_model.name = "Random Strategy"
        # Pattern Strategy
        pattern_model = PatternStrategy(df_pd, time_predict=time_predict, min_val=config.min_value, max_val=config.max_value)
        pattern_model.number_predict = config.size_output
        pattern_model.name = "Pattern Strategy"
        # Pair Frequency Strategy
        pair_frequency_model = PairFrequencyStrategy(df_pd, time_predict=time_predict, min_val=config.min_value, max_val=config.max_value)
        pair_frequency_model.number_predict = config.size_output
        pair_frequency_model.name = "Pair Frequency Strategy"
        # Not repeat
        not_repeat_model = RandomModel(df_pd, time_predict=time_predict, min_val=config.min_value, max_val=config.max_value)
        not_repeat_model.number_predict = config.size_output
        not_repeat_model.name = "Not Repeat Strategy"
        # Markov chain strategy
        markov_chain_model = RandomModel(df_pd, time_predict=time_predict, min_val=config.min_value, max_val=config.max_value)
        markov_chain_model.number_predict = config.size_output
        markov_chain_model.name = "Markov Chain Strategy"
        # Long absence strategy
        long_absence_model = RandomModel(df_pd, time_predict=time_predict, min_val=config.min_value, max_val=config.max_value)
        long_absence_model.number_predict = config.size_output
        long_absence_model.name = "Long Absence Strategy"
        # Frequency strategy
        frequency_model = RandomModel(df_pd, time_predict=time_predict, min_val=config.min_value, max_val=config.max_value)
        frequency_model.number_predict = config.size_output
        frequency_model.name = "Frequency Strategy"
        # Exponential decay strategy
        exponential_decay_model = RandomModel(df_pd, time_predict=time_predict, min_val=config.min_value, max_val=config.max_value)
        exponential_decay_model.number_predict = config.size_output
        exponential_decay_model.name = "Exponential Decay Strategy"
        models = [random_model, pattern_model, pair_frequency_model, not_repeat_model, 
                  markov_chain_model, long_absence_model, frequency_model, exponential_decay_model]

        for model in models:
            for _ in range(number):
                ticket = model.predict(next_draw_date)
                prediction_records.append({
                    "date": next_draw_date_str,
                    "result": ticket,
                    "odd_even": analyze_odd_even_counter(ticket),
                    "strategy": model.name,
                })
            # logger.debug(f"Generated {prediction_records} predictions for {product} using {name}.")
            if prediction_records:
                df_predictions = pd.DataFrame(prediction_records)
                df_predictions = df_predictions.sort_values(by=["date", "strategy"], ascending=False)
                output_path = f"./data/prediction/{product}_prediction.jsonl"
                save_predictions(df_predictions, output_path)
                
        logger.info("\n✅ All demos completed successfully!")
    except Exception as e:
        logger.error(f"Demo failed: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VietLott Strategies")
    parser.add_argument("--product", type=str, default="power_645", choices=["power_645", "power_655", "power_535"], help="The lottery product")
    parser.add_argument("--number", type=int, default=10, help="The number of predictions to generate")
    args = parser.parse_args()
    main(args.product, args.number)
