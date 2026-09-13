# Author: Cong Pham <chicong7891@gmail.com>

from datetime import timedelta
from pathlib import Path

import attr

cwd = Path(__file__).parent
project_root = Path(__file__).parent.parent.parent

data_dir = project_root.parent / "data"

@attr.define
class ProductConfig:
    name: str
    raw_path: Path
    min_value: int
    max_value: int
    size_output: int
    interval: timedelta
    num_thread: int = 10
    use_cookies: bool = True
    default_index_to: int = 1
    page_size: int = 6
    prediction_path: Path = attr.field(factory=lambda: data_dir / "prediction" / "default_prediction.jsonl")
    analysis_path: Path = attr.field(factory=lambda: data_dir / "analysis" / "default_analysis.jsonl")
    days_of_week: list[int] = attr.field(factory=lambda: [1, 2, 3, 4, 5, 6, 7])  # Default to all days of the week (1=Monday, 7=Sunday)
    time_range: list[str] = [] # Optional time range for draws, e.g., ["18:00", "20:00"] for products like power_645 and power_655
    time: list[str] = []  # Optional specific draw times, e.g., ["13:00", "21:00"] for products like power_535

power655_config = ProductConfig(
    name="power_655",
    raw_path=data_dir / "raw" / "power655.jsonl",
    min_value=1,
    max_value=55,
    size_output=6,
    interval=timedelta(days=2),
    use_cookies=False,
    prediction_path=data_dir / "prediction" / "power_655_prediction.jsonl",
    analysis_path=data_dir / "analysis" / "power_655_analysis.jsonl",
    days_of_week=[1, 3, 5],  # Draws on Monday, Wednesday, Friday
    time_range=["18:00", "20:00"],  # Draws between 6 PM and 8 PM
)
power645_config = ProductConfig(
    name="power_645",
    raw_path=data_dir / "raw" / "power645.jsonl",
    min_value=1,
    max_value=45,
    size_output=6,
    interval=timedelta(days=2),
    use_cookies=False,
    prediction_path=data_dir / "prediction" / "power_645_prediction.jsonl",
    analysis_path=data_dir / "analysis" / "power_645_analysis.jsonl",
    days_of_week=[2, 4, 6],  # Draws on Tuesday, Thursday, Saturday
    time_range=["18:00", "18:30"]  # Draws between 6 PM and 6:30 PM
)
power535_config = ProductConfig(
    name="power_535",
    raw_path=data_dir / "raw" / "power535.jsonl",
    min_value=1,
    max_value=35,
    size_output=5,
    interval=timedelta(days=2),
    use_cookies=False,
    prediction_path=data_dir / "prediction" / "power_535_prediction.jsonl",
    analysis_path=data_dir / "analysis" / "power_535_analysis.jsonl",
    days_of_week=[1, 2, 3, 4, 5, 6, 7],  # Draws on all days of the week
    time=["13:00", "21:00"]  # Draws at 1 PM and 9 PM
)
keno_config = ProductConfig(
    name="keno",
    raw_path=data_dir / "raw" / "keno.jsonl",
    min_value=1,
    max_value=45,
    size_output=6,
    interval=timedelta(minutes=8),
    default_index_to=24,
    num_thread=20,
    page_size=6,
    use_cookies=False,
    prediction_path=data_dir / "prediction" / "keno_prediction.jsonl",
    analysis_path=data_dir / "analysis" / "keno_analysis.jsonl",
)

p3d_config = ProductConfig(
    name="3d",
    raw_path=data_dir / "raw" / "3d.jsonl",
    min_value=0,
    max_value=999,
    size_output=6,
    interval=timedelta(days=2),
    default_index_to=1,
    num_thread=20,
    page_size=5,
    use_cookies=False,
    prediction_path=data_dir / "prediction" / "3d_prediction.jsonl",
    analysis_path=data_dir / "analysis" / "3d_analysis.jsonl",
)

p3d_pro_config = ProductConfig(
    name="3d_pro",
    raw_path=data_dir / "raw" / "3d_pro.jsonl",
    min_value=0,
    max_value=999,
    size_output=6,
    interval=timedelta(days=2),
    default_index_to=1,
    num_thread=20,
    page_size=5,
    use_cookies=False,
    prediction_path=data_dir / "prediction" / "3d_pro_prediction.jsonl",
    analysis_path=data_dir / "analysis" / "3d_pro_analysis.jsonl",
)

bingo18_config = ProductConfig(
    name="bingo18",
    raw_path=data_dir / "raw" / "bingo18.jsonl",
    min_value=0,
    max_value=9,
    size_output=3,
    interval=timedelta(minutes=5),  # Bingo18 runs frequently throughout the day
    default_index_to=1,
    num_thread=10,
    page_size=6,
    use_cookies=False,
    prediction_path=data_dir / "prediction" / "bingo18_prediction.jsonl",
    analysis_path=data_dir / "analysis" / "bingo18_analysis.jsonl",
)

product_config_map = {
    c.name: c
    for c in [
        power645_config,
        power655_config,
        power535_config,
        keno_config,
        p3d_config,
        p3d_pro_config,
        bingo18_config,
    ]
}


def get_config(name: str) -> ProductConfig:
    if name in product_config_map:
        return product_config_map[name]
    else:
        raise ValueError(f"Unknown product: {name}")
