from typing import List, Dict, Any, Set

def calculate_matches(
    prediction_numbers: List[int],
    actual_numbers: List[int],
    is_special_product: bool = False
) -> Dict[str, Any]:
    """
    Compares a predicted ticket with the actual results to find matches.

    For special products (power655, power535), it compares only the main numbers.
    """
    pred_set = set(prediction_numbers[:-1] if is_special_product else prediction_numbers)
    actual_set = set(actual_numbers[:-1] if is_special_product else actual_numbers)
    match_result: Set[int] = pred_set.intersection(actual_set)
    result = {
        'matches_count': len(match_result),
        'matches_result': sorted(list(match_result)),
    }
    if is_special_product:
      if prediction_numbers[-1] == actual_numbers[-1]:
        result['matches_special_number'] = True
      else:
        result['matches_special_number'] = False
        
    return result