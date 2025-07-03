# 🎰 Vietlott Data

[![GitHub Actions](https://github.com/vietvudanh/vietlott-data/workflows/crawl/badge.svg)](https://github.com/vietvudanh/vietlott-data/actions)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/vietvudanh/vietlott-data/commits/main)

> 📊 **Automated Vietnamese Lottery Data Collection & Analysis**
> 
> This project automatically crawls and analyzes Vietnamese lottery data from [vietlott.vn](https://vietlott.vn/), providing comprehensive statistics and insights for all major lottery products.

## 🎯 Supported Lottery Products

| Product | Link | Description |
|---------|------|-------------|
| **Power 6/55** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655) | Choose 6 numbers from 1-55 |
| **Power 6/45** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645) | Choose 6 numbers from 1-45 |
| **Keno** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno) | Fast-pace number game |
| **Max 3D** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d) | 3-digit lottery game |
| **Max 3D Pro** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro) | Enhanced 3D lottery |
| **Bingo18** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-bingo18) | 3 numbers from 0-9 game |


## 📋 Table of Contents

- [🎯 Supported Lottery Products](#-supported-lottery-products)
- [📊 Data Statistics](#-data-statistics)
- [🔮 Prediction Models](#-prediction-models)
- [📈 Power 6/55 Analysis](#-power-655-analysis)
  - [📅 Recent Results](#-recent-results)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)


## 📊 Data Statistics

| Product   |   Total Draws | Start Date   | End Date   |   Total Records | First ID   | Latest ID   |
|:----------|--------------:|:-------------|:-----------|----------------:|:-----------|:------------|
| Power 655 |          1210 | 2017-08-01   | 2025-07-01 |            1210 | 00001      | 01210       |
| Power 645 |          1177 | 2017-10-25   | 2025-07-02 |            1177 | 00198      | 01374       |
| Keno      |           939 | 2022-12-04   | 2025-07-03 |          132645 | #0110271   | #0243542    |
| 3D        |           945 | 2019-04-22   | 2025-07-02 |             945 | 00001      | 00945       |
| 3D Pro    |           591 | 2021-09-14   | 2025-07-01 |             591 | 00001      | 00591       |
| Bingo18   |           213 | 2024-12-03   | 2025-07-03 |           33619 | 0083123    | 0116789     |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

No significant matches found in backtest period.



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-07-01 | 01210 | [3, 11, 12, 14, 27, 33, 15]  |      0 | 2025-07-02 00:01:16.154567 |
| 2025-06-28 | 01209 | [8, 11, 13, 20, 45, 50, 25]  |      0 | 2025-06-30 15:30:00.150910 |
| 2025-06-26 | 01208 | [1, 14, 16, 27, 40, 51, 2]   |      0 | 2025-06-30 15:30:00.151037 |
| 2025-06-24 | 01207 | [3, 9, 18, 20, 30, 53, 48]   |      0 | 2025-06-30 15:30:00.151131 |
| 2025-06-21 | 01206 | [6, 10, 15, 43, 44, 53, 32]  |      0 | 2025-06-22 19:00:16.907461 |
| 2025-06-19 | 01205 | [3, 5, 9, 10, 16, 47, 34]    |      0 | 2025-06-19 19:00:12.105342 |
| 2025-06-17 | 01204 | [7, 13, 18, 22, 32, 44, 43]  |      0 | 2025-06-17 19:00:14.248629 |
| 2025-06-14 | 01203 | [11, 12, 22, 26, 41, 47, 24] |      0 | 2025-06-15 19:00:27.381690 |
| 2025-06-12 | 01202 | [6, 8, 16, 18, 34, 44, 17]   |      0 | 2025-06-12 19:00:09.940893 |
| 2025-06-10 | 01201 | [3, 6, 21, 29, 40, 41, 37]   |      0 | 2025-06-11 19:00:17.010268 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     167 | 1.97 |     |       21 |     151 | 1.78 |     | 41       | 183     | 2.16 |
|        2 |     141 | 1.66 |     |       22 |     173 | 2.04 |     | 42       | 157     | 1.85 |
|        3 |     167 | 1.97 |     |       23 |     167 | 1.97 |     | 43       | 172     | 2.03 |
|        4 |     131 | 1.55 |     |       24 |     154 | 1.82 |     | 44       | 160     | 1.89 |
|        5 |     152 | 1.79 |     |       25 |     140 | 1.65 |     | 45       | 151     | 1.78 |
|        6 |     131 | 1.55 |     |       26 |     142 | 1.68 |     | 46       | 159     | 1.88 |
|        7 |     134 | 1.58 |     |       27 |     142 | 1.68 |     | 47       | 158     | 1.87 |
|        8 |     162 | 1.91 |     |       28 |     135 | 1.59 |     | 48       | 163     | 1.92 |
|        9 |     168 | 1.98 |     |       29 |     162 | 1.91 |     | 49       | 158     | 1.87 |
|       10 |     144 | 1.7  |     |       30 |     134 | 1.58 |     | 50       | 156     | 1.84 |
|       11 |     162 | 1.91 |     |       31 |     157 | 1.85 |     | 51       | 176     | 2.08 |
|       12 |     163 | 1.92 |     |       32 |     159 | 1.88 |     | 52       | 158     | 1.87 |
|       13 |     148 | 1.75 |     |       33 |     153 | 1.81 |     | 53       | 162     | 1.91 |
|       14 |     155 | 1.83 |     |       34 |     170 | 2.01 |     | 54       | 145     | 1.71 |
|       15 |     146 | 1.72 |     |       35 |     151 | 1.78 |     | 55       | 152     | 1.79 |
|       16 |     144 | 1.7  |     |       36 |     142 | 1.68 |     |          |         |      |
|       17 |     141 | 1.66 |     |       37 |     141 | 1.66 |     |          |         |      |
|       18 |     157 | 1.85 |     |       38 |     144 | 1.7  |     |          |         |      |
|       19 |     152 | 1.79 |     |       39 |     146 | 1.72 |     |          |         |      |
|       20 |     164 | 1.94 |     |       40 |     167 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |   % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       1 | 1.1 |     |       24 |       1 | 1.1 |     | 50       | 1       | 1.1 |
|        2 |       2 | 2.2 |     |       25 |       1 | 1.1 |     | 51       | 2       | 2.2 |
|        3 |       4 | 4.4 |     |       26 |       1 | 1.1 |     | 52       | 1       | 1.1 |
|        5 |       1 | 1.1 |     |       27 |       3 | 3.3 |     | 53       | 2       | 2.2 |
|        6 |       3 | 3.3 |     |       29 |       1 | 1.1 |     |          |         |     |
|        7 |       1 | 1.1 |     |       30 |       1 | 1.1 |     |          |         |     |
|        8 |       2 | 2.2 |     |       32 |       2 | 2.2 |     |          |         |     |
|        9 |       2 | 2.2 |     |       33 |       2 | 2.2 |     |          |         |     |
|       10 |       2 | 2.2 |     |       34 |       3 | 3.3 |     |          |         |     |
|       11 |       4 | 4.4 |     |       37 |       2 | 2.2 |     |          |         |     |
|       12 |       3 | 3.3 |     |       38 |       1 | 1.1 |     |          |         |     |
|       13 |       2 | 2.2 |     |       40 |       2 | 2.2 |     |          |         |     |
|       14 |       4 | 4.4 |     |       41 |       2 | 2.2 |     |          |         |     |
|       15 |       2 | 2.2 |     |       43 |       2 | 2.2 |     |          |         |     |
|       16 |       4 | 4.4 |     |       44 |       3 | 3.3 |     |          |         |     |
|       17 |       2 | 2.2 |     |       45 |       2 | 2.2 |     |          |         |     |
|       18 |       3 | 3.3 |     |       46 |       2 | 2.2 |     |          |         |     |
|       20 |       2 | 2.2 |     |       47 |       2 | 2.2 |     |          |         |     |
|       21 |       3 | 3.3 |     |       48 |       2 | 2.2 |     |          |         |     |
|       22 |       2 | 2.2 |     |       49 |       1 | 1.1 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.57 |     |       21 |       4 | 2.29 |     | 45       | 6       | 3.43 |
|        2 |       3 | 1.71 |     |       22 |       3 | 1.71 |     | 46       | 3       | 1.71 |
|        3 |       6 | 3.43 |     |       24 |       3 | 1.71 |     | 47       | 5       | 2.86 |
|        4 |       1 | 0.57 |     |       25 |       2 | 1.14 |     | 48       | 3       | 1.71 |
|        5 |       2 | 1.14 |     |       26 |       2 | 1.14 |     | 49       | 3       | 1.71 |
|        6 |       5 | 2.86 |     |       27 |       5 | 2.86 |     | 50       | 4       | 2.29 |
|        7 |       4 | 2.29 |     |       28 |       2 | 1.14 |     | 51       | 3       | 1.71 |
|        8 |       4 | 2.29 |     |       29 |       3 | 1.71 |     | 52       | 2       | 1.14 |
|        9 |       5 | 2.86 |     |       30 |       3 | 1.71 |     | 53       | 2       | 1.14 |
|       10 |       2 | 1.14 |     |       32 |       2 | 1.14 |     | 54       | 2       | 1.14 |
|       11 |       4 | 2.29 |     |       33 |       2 | 1.14 |     | 55       | 4       | 2.29 |
|       12 |       5 | 2.86 |     |       34 |       4 | 2.29 |     |          |         |      |
|       13 |       3 | 1.71 |     |       37 |       4 | 2.29 |     |          |         |      |
|       14 |       7 | 4    |     |       38 |       1 | 0.57 |     |          |         |      |
|       15 |       5 | 2.86 |     |       39 |       3 | 1.71 |     |          |         |      |
|       16 |       6 | 3.43 |     |       40 |       2 | 1.14 |     |          |         |      |
|       17 |       2 | 1.14 |     |       41 |       5 | 2.86 |     |          |         |      |
|       18 |       4 | 2.29 |     |       42 |       3 | 1.71 |     |          |         |      |
|       19 |       4 | 2.29 |     |       43 |       3 | 1.71 |     |          |         |      |
|       20 |       3 | 1.71 |     |       44 |       6 | 3.43 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.13 |     |       21 |       6 | 2.26 |     | 42       | 8       | 3.01 |
|        2 |       4 | 1.5  |     |       22 |       3 | 1.13 |     | 43       | 7       | 2.63 |
|        3 |      10 | 3.76 |     |       23 |       4 | 1.5  |     | 44       | 6       | 2.26 |
|        4 |       1 | 0.38 |     |       24 |       5 | 1.88 |     | 45       | 7       | 2.63 |
|        5 |       3 | 1.13 |     |       25 |       3 | 1.13 |     | 46       | 3       | 1.13 |
|        6 |       5 | 1.88 |     |       26 |       3 | 1.13 |     | 47       | 7       | 2.63 |
|        7 |       5 | 1.88 |     |       27 |       6 | 2.26 |     | 48       | 5       | 1.88 |
|        8 |       5 | 1.88 |     |       28 |       3 | 1.13 |     | 49       | 5       | 1.88 |
|        9 |       6 | 2.26 |     |       29 |       5 | 1.88 |     | 50       | 5       | 1.88 |
|       10 |       4 | 1.5  |     |       30 |       3 | 1.13 |     | 51       | 3       | 1.13 |
|       11 |       5 | 1.88 |     |       31 |       2 | 0.75 |     | 52       | 4       | 1.5  |
|       12 |       5 | 1.88 |     |       32 |       5 | 1.88 |     | 53       | 3       | 1.13 |
|       13 |       5 | 1.88 |     |       33 |       3 | 1.13 |     | 54       | 2       | 0.75 |
|       14 |      10 | 3.76 |     |       34 |       5 | 1.88 |     | 55       | 5       | 1.88 |
|       15 |      10 | 3.76 |     |       36 |       1 | 0.38 |     |          |         |      |
|       16 |       7 | 2.63 |     |       37 |       7 | 2.63 |     |          |         |      |
|       17 |       4 | 1.5  |     |       38 |       3 | 1.13 |     |          |         |      |
|       18 |       5 | 1.88 |     |       39 |       4 | 1.5  |     |          |         |      |
|       19 |       7 | 2.63 |     |       40 |       5 | 1.88 |     |          |         |      |
|       20 |       5 | 1.88 |     |       41 |      11 | 4.14 |     |          |         |      |



## ⚙️ How It Works

### 🤖 Automated Data Collection

This project runs completely automatically using **GitHub Actions** - no server required!

- **⏰ Schedule**: Runs daily via [GitHub Actions workflow](.github/workflows/crawl.yaml)
- **🔄 Process**: Fetches latest results → Processes data → Commits to repository
- **📊 Analysis**: Generates statistics and updates README automatically

### 🕵️ Data Crawling Method

The data collection works by:
1. **🔍 Network Analysis**: Inspecting browser-server communication
2. **🐍 Python Replication**: Recreating the data fetch logic in Python
3. **📋 Structured Storage**: Saving results in JSONL format for easy analysis
4. **🔄 Continuous Updates**: Daily automated runs ensure fresh data

> **Note**: This is purely for educational and research purposes. No gambling advice is provided.


## 🚀 Installation & Usage

### 📦 Install via pip

```bash
pip install -i https://test.pypi.org/simple/ vietlott-data==0.1.3
```

### 💻 Command Line Interface

#### 🔍 Crawl Data

```bash
vietlott-crawl [OPTIONS] PRODUCT

# Options:
#   --run-date TEXT       Specific date to crawl
#   --index_from INTEGER  Starting page index
#   --index_to INTEGER    Ending page index
#   --help               Show help message
```

#### 🔧 Backfill Missing Data

```bash
vietlott-missing [OPTIONS] PRODUCT

# Options:
#   --limit INTEGER  Number of pages to process
#   --help          Show help message
```

### 🛠️ Development Setup

```bash
# Clone the repository
git clone https://github.com/vietvudanh/vietlott-data.git
cd vietlott-data

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <strong>⭐ If you find this project useful, please consider giving it a star!</strong>
</div>

