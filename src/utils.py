# Author: Cong Pham <chicong7891@gmail.com>
from datetime import datetime, time, timedelta
from typing import List, Dict, Any, Set
from loguru import logger
import pandas as pd

def save_predictions(df_new_predictions: pd.DataFrame, file_path: str):
    """Reads an existing prediction file, prepends new predictions, and saves it."""
    try:
        # Read existing data if the file exists and is not empty
        existing_df = pd.read_json(file_path, lines=True, convert_dates=False)
        # Prepend new predictions to the existing ones
        combined_df = pd.concat([df_new_predictions, existing_df], ignore_index=True)
    except (FileNotFoundError, ValueError):  # Handles non-existent or empty/invalid files
        combined_df = df_new_predictions

    combined_df.to_json(file_path, orient="records", lines=True, date_format="iso")
    logger.info(f"Saved {len(df_new_predictions)} new predictions to the top of {file_path}")

def get_next_draw_date(lottery_config: Dict[str, Any]) -> str:
    """Calculates the next draw date for a given product based on the schedule."""
    logger.debug(f"Loaded lottery schedule: {lottery_config}")
    # Handle multi-time products like power_535
    if len(lottery_config.get("time", [])) > 0:
        now = datetime.now()
        draw_times_str = sorted(lottery_config.get("time", []))
        draw_times = [time.fromisoformat(t) for t in draw_times_str]

        # Find the next draw time for today
        for draw_time in draw_times:
            if now.time() < draw_time:
                return now.strftime(f"%Y-%m-%d {draw_time.strftime('%H:%M')}")

        # If all of today's draws are over, get the first draw of the next day
        next_day = now + datetime.timedelta(days=1)
        first_draw_time = draw_times[0]
        return next_day.strftime(f"%Y-%m-%d {first_draw_time.strftime('%H:%M')}")
    
    # Lấy thông tin từ cấu hình
    days_of_week = lottery_config["days_of_week"]  # [3, 5, 7] -> Thứ 4, Thứ 6, Chủ Nhật
    end_time_str = lottery_config["time_range"][1] # "18:30"
    
    # Lấy thời gian hiện tại
    now = datetime.now()
    current_date = now.date()
    
    # Chuyển đổi giờ kết thúc quay thưởng sang đối tượng time
    end_time = datetime.strptime(end_time_str, "%H:%M").time()
    
    # Vòng lặp kiểm tra từ ngày hôm nay (cộng thêm 0 đến 7 ngày)
    for i in range(8):
        check_date = current_date + timedelta(days=i)
        # Trong Python .isoweekday() trả về: Thứ 2 = 1, ..., Thứ 4 = 3, Thứ 6 = 5, Chủ Nhật = 7
        if check_date.isoweekday() in days_of_week:
            # Nếu là ngày hôm nay, phải kiểm tra xem đã quá giờ quay thưởng chưa
            if i == 0 and now.time() > end_time:
                continue  # Nếu quá giờ rồi thì bỏ qua hôm nay, tìm ngày tiếp theo
            return check_date.strftime("%Y-%m-%d")

def analyze_odd_even_counter(ticket: list[int]) -> str:
      """Calculates the odd/even split for a ticket and returns it as a string 'odd:even'."""
      odd_count = sum(1 for num in ticket if num % 2 != 0)
      even_count = len(ticket) - odd_count
      return f"{odd_count}:{even_count}"

def calculate_matches(
    prediction_numbers: List[int],
    actual_numbers: List[int],
    is_special_product: bool = False
) -> Dict[str, Any]:
    """
    Compares a predicted ticket with the actual results to find matches.

    For special products (power_655, power_645, power_535), it compares only the main numbers.
    """
    pred_set = set(prediction_numbers[:-1] if is_special_product else prediction_numbers)
    actual_set = set(actual_numbers[:-1] if is_special_product else actual_numbers)
    match_result: Set[int] = pred_set.intersection(actual_set)
    result = {
        'matches_count': len(match_result),
        'matches_result': sorted(match_result),
    }
    if is_special_product:
      if prediction_numbers[-1] == actual_numbers[-1]:
        result['matches_special_number'] = True
      else:
        result['matches_special_number'] = False
        
    return result