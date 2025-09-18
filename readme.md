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
| **Power 5/35** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/535) | Choose 5 numbers from 1-35 |
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
- [📈 Power 5/35 Analysis](#-power-535-analysis)
  - [📅 Recent Results](#-recent-results-1)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time-1)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period-1)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)


## 📊 Data Statistics

| Product   |   Total Draws | Start Date   | End Date   |   Total Records | First ID   | Latest ID   |
|:----------|--------------:|:-------------|:-----------|----------------:|:-----------|:------------|
| Power 655 |          1244 | 2017-08-01   | 2025-09-18 |            1244 | 00001      | 01244       |
| Power 645 |          1407 | 2016-07-20   | 2025-09-17 |            1407 | 00001      | 01407       |
| Power 535 |            71 | 2025-06-29   | 2025-09-18 |             140 | 00001      | 00164       |
| Keno      |           322 | 2022-12-04   | 2025-09-18 |           42454 | #0110271   | #0252777    |
| 3D        |           978 | 2019-04-22   | 2025-09-17 |             978 | 00001      | 00978       |
| 3D Pro    |           625 | 2021-09-14   | 2025-09-18 |             625 | 00001      | 00625       |
| Bingo18   |           276 | 2024-12-03   | 2025-09-18 |           43515 | 0083123    | 0129131     |

## 🔮 Prediction Models 6/55

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
| 2025-09-18 | 01244 | [2, 3, 8, 27, 38, 55, 20]    |      0 | 2025-09-18 22:07:03.049329 |
| 2025-09-16 | 01243 | [17, 19, 28, 39, 43, 53, 33] |      0 | 2025-09-18 22:07:03.049435 |
| 2025-09-13 | 01242 | [2, 7, 15, 18, 24, 27, 45]   |      0 | 2025-09-18 22:07:03.049534 |
| 2025-09-11 | 01241 | [6, 16, 46, 49, 51, 55, 42]  |      0 | 2025-09-18 22:07:03.049630 |
| 2025-09-09 | 01240 | [16, 20, 21, 31, 40, 52, 2]  |      0 | 2025-09-18 22:07:03.049727 |
| 2025-09-06 | 01239 | [9, 11, 19, 22, 34, 43, 31]  |      0 | 2025-09-18 22:07:03.049822 |
| 2025-09-04 | 01238 | [9, 19, 23, 42, 49, 53, 40]  |      0 | 2025-09-18 22:07:03.049916 |
| 2025-09-02 | 01237 | [9, 16, 22, 25, 30, 51, 43]  |      0 | 2025-09-03 09:49:14.784413 |
| 2025-08-30 | 01236 | [2, 17, 19, 24, 30, 44, 34]  |      0 | 2025-08-31 12:07:10.223130 |
| 2025-08-28 | 01235 | [6, 13, 28, 30, 35, 52, 50]  |      0 | 2025-08-30 10:11:29.649921 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     170 | 1.95 |     |       21 |     152 | 1.75 |     | 41       | 186     | 2.14 |
|        2 |     146 | 1.68 |     |       22 |     178 | 2.04 |     | 42       | 162     | 1.86 |
|        3 |     170 | 1.95 |     |       23 |     171 | 1.96 |     | 43       | 177     | 2.03 |
|        4 |     132 | 1.52 |     |       24 |     161 | 1.85 |     | 44       | 167     | 1.92 |
|        5 |     159 | 1.83 |     |       25 |     141 | 1.62 |     | 45       | 159     | 1.83 |
|        6 |     136 | 1.56 |     |       26 |     145 | 1.67 |     | 46       | 161     | 1.85 |
|        7 |     135 | 1.55 |     |       27 |     145 | 1.67 |     | 47       | 161     | 1.85 |
|        8 |     166 | 1.91 |     |       28 |     140 | 1.61 |     | 48       | 170     | 1.95 |
|        9 |     176 | 2.02 |     |       29 |     166 | 1.91 |     | 49       | 161     | 1.85 |
|       10 |     148 | 1.7  |     |       30 |     140 | 1.61 |     | 50       | 159     | 1.83 |
|       11 |     163 | 1.87 |     |       31 |     166 | 1.91 |     | 51       | 183     | 2.1  |
|       12 |     165 | 1.9  |     |       32 |     164 | 1.88 |     | 52       | 164     | 1.88 |
|       13 |     150 | 1.72 |     |       33 |     159 | 1.83 |     | 53       | 168     | 1.93 |
|       14 |     157 | 1.8  |     |       34 |     179 | 2.06 |     | 54       | 149     | 1.71 |
|       15 |     149 | 1.71 |     |       35 |     155 | 1.78 |     | 55       | 157     | 1.8  |
|       16 |     148 | 1.7  |     |       36 |     147 | 1.69 |     |          |         |      |
|       17 |     146 | 1.68 |     |       37 |     143 | 1.64 |     |          |         |      |
|       18 |     162 | 1.86 |     |       38 |     146 | 1.68 |     |          |         |      |
|       19 |     158 | 1.81 |     |       39 |     150 | 1.72 |     |          |         |      |
|       20 |     167 | 1.92 |     |       40 |     172 | 1.98 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 2.04 |     |       24 |       2 | 2.04 |     | 47       | 1       | 1.02 |
|        2 |       4 | 4.08 |     |       25 |       1 | 1.02 |     | 48       | 1       | 1.02 |
|        3 |       1 | 1.02 |     |       26 |       1 | 1.02 |     | 49       | 2       | 2.04 |
|        5 |       2 | 2.04 |     |       27 |       2 | 2.04 |     | 50       | 2       | 2.04 |
|        6 |       2 | 2.04 |     |       28 |       2 | 2.04 |     | 51       | 2       | 2.04 |
|        7 |       1 | 1.02 |     |       30 |       4 | 4.08 |     | 52       | 3       | 3.06 |
|        8 |       1 | 1.02 |     |       31 |       3 | 3.06 |     | 53       | 2       | 2.04 |
|        9 |       5 | 5.1  |     |       33 |       1 | 1.02 |     | 55       | 3       | 3.06 |
|       11 |       1 | 1.02 |     |       34 |       4 | 4.08 |     |          |         |      |
|       13 |       1 | 1.02 |     |       35 |       2 | 2.04 |     |          |         |      |
|       14 |       1 | 1.02 |     |       36 |       1 | 1.02 |     |          |         |      |
|       15 |       1 | 1.02 |     |       38 |       2 | 2.04 |     |          |         |      |
|       16 |       3 | 3.06 |     |       39 |       1 | 1.02 |     |          |         |      |
|       17 |       3 | 3.06 |     |       40 |       3 | 3.06 |     |          |         |      |
|       18 |       1 | 1.02 |     |       41 |       1 | 1.02 |     |          |         |      |
|       19 |       4 | 4.08 |     |       42 |       2 | 2.04 |     |          |         |      |
|       20 |       2 | 2.04 |     |       43 |       3 | 3.06 |     |          |         |      |
|       21 |       1 | 1.02 |     |       44 |       4 | 4.08 |     |          |         |      |
|       22 |       3 | 3.06 |     |       45 |       2 | 2.04 |     |          |         |      |
|       23 |       1 | 1.02 |     |       46 |       1 | 1.02 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.65 |     |       21 |       1 | 0.55 |     | 41       | 2       | 1.1  |
|        2 |       4 | 2.2  |     |       22 |       4 | 2.2  |     | 42       | 3       | 1.65 |
|        3 |       1 | 0.55 |     |       23 |       3 | 1.65 |     | 43       | 5       | 2.75 |
|        4 |       1 | 0.55 |     |       24 |       6 | 3.3  |     | 44       | 5       | 2.75 |
|        5 |       7 | 3.85 |     |       25 |       1 | 0.55 |     | 45       | 5       | 2.75 |
|        6 |       5 | 2.75 |     |       26 |       2 | 1.1  |     | 46       | 2       | 1.1  |
|        7 |       1 | 0.55 |     |       27 |       2 | 1.1  |     | 47       | 3       | 1.65 |
|        8 |       3 | 1.65 |     |       28 |       4 | 2.2  |     | 48       | 4       | 2.2  |
|        9 |       7 | 3.85 |     |       29 |       3 | 1.65 |     | 49       | 3       | 1.65 |
|       10 |       4 | 2.2  |     |       30 |       5 | 2.75 |     | 50       | 2       | 1.1  |
|       11 |       1 | 0.55 |     |       31 |       6 | 3.3  |     | 51       | 5       | 2.75 |
|       12 |       1 | 0.55 |     |       32 |       3 | 1.65 |     | 52       | 5       | 2.75 |
|       13 |       1 | 0.55 |     |       33 |       4 | 2.2  |     | 53       | 4       | 2.2  |
|       14 |       2 | 1.1  |     |       34 |       7 | 3.85 |     | 54       | 1       | 0.55 |
|       15 |       2 | 1.1  |     |       35 |       4 | 2.2  |     | 55       | 4       | 2.2  |
|       16 |       4 | 2.2  |     |       36 |       3 | 1.65 |     |          |         |      |
|       17 |       5 | 2.75 |     |       37 |       2 | 1.1  |     |          |         |      |
|       18 |       2 | 1.1  |     |       38 |       2 | 1.1  |     |          |         |      |
|       19 |       5 | 2.75 |     |       39 |       2 | 1.1  |     |          |         |      |
|       20 |       2 | 1.1  |     |       40 |       4 | 2.2  |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.47 |     |       21 |       1 | 0.37 |     | 41       | 3       | 1.1  |
|        2 |       6 | 2.2  |     |       22 |       5 | 1.83 |     | 42       | 5       | 1.83 |
|        3 |       5 | 1.83 |     |       23 |       4 | 1.47 |     | 43       | 6       | 2.2  |
|        4 |       1 | 0.37 |     |       24 |       7 | 2.56 |     | 44       | 8       | 2.93 |
|        5 |       7 | 2.56 |     |       25 |       2 | 0.73 |     | 45       | 9       | 3.3  |
|        6 |       6 | 2.2  |     |       26 |       3 | 1.1  |     | 46       | 2       | 0.73 |
|        7 |       1 | 0.37 |     |       27 |       5 | 1.83 |     | 47       | 3       | 1.1  |
|        8 |       5 | 1.83 |     |       28 |       5 | 1.83 |     | 48       | 8       | 2.93 |
|        9 |       9 | 3.3  |     |       29 |       4 | 1.47 |     | 49       | 3       | 1.1  |
|       10 |       5 | 1.83 |     |       30 |       7 | 2.56 |     | 50       | 4       | 1.47 |
|       11 |       3 | 1.1  |     |       31 |       9 | 3.3  |     | 51       | 8       | 2.93 |
|       12 |       3 | 1.1  |     |       32 |       6 | 2.2  |     | 52       | 6       | 2.2  |
|       13 |       3 | 1.1  |     |       33 |       7 | 2.56 |     | 53       | 8       | 2.93 |
|       14 |       4 | 1.47 |     |       34 |       9 | 3.3  |     | 54       | 4       | 1.47 |
|       15 |       5 | 1.83 |     |       35 |       4 | 1.47 |     | 55       | 5       | 1.83 |
|       16 |       5 | 1.83 |     |       36 |       5 | 1.83 |     |          |         |      |
|       17 |       5 | 1.83 |     |       37 |       2 | 0.73 |     |          |         |      |
|       18 |       6 | 2.2  |     |       38 |       2 | 0.73 |     |          |         |      |
|       19 |       6 | 2.2  |     |       39 |       4 | 1.47 |     |          |         |      |
|       20 |       5 | 1.83 |     |       40 |       6 | 2.2  |     |          |         |      |



### ⚖️ [6/55] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 417        | 33.52     |
| 2:4                  | 311        | 25.00     |
| 4:2                  | 295        | 23.71     |
| 5:1                  | 117        | 9.41      |
| 1:5                  | 77         | 6.19      |
| 6:0                  | 20         | 1.61      |
| 0:6                  | 7          | 0.56      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 5          | 35.71     |
| 2:4                  | 4          | 28.57     |
| 5:1                  | 3          | 21.43     |
| 4:2                  | 1          | 7.14      |
| 1:5                  | 1          | 7.14      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 9          | 34.62     |
| 2:4                  | 8          | 30.77     |
| 4:2                  | 5          | 19.23     |
| 5:1                  | 3          | 11.54     |
| 1:5                  | 1          | 3.85      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 15         | 38.46     |
| 2:4                  | 10         | 25.64     |
| 4:2                  | 7          | 17.95     |
| 5:1                  | 4          | 10.26     |
| 1:5                  | 3          | 7.69      |


## 🔮 Prediction Models 6/45

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                   | predicted                |
|:-----------|:-------------------------|:-------------------------|
| 2021-08-18 | [10, 16, 19, 27, 28, 36] | [16, 36, 28, 10, 19, 25] |



## 📈 Power 6/45 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                   |   page | process_time               |
|:-----------|------:|:-------------------------|-------:|:---------------------------|
| 2025-09-17 | 01407 | [11, 23, 25, 35, 38, 45] |      0 | 2025-09-18T22:07:07.851469 |
| 2025-09-14 | 01406 | [3, 6, 9, 10, 30, 37]    |      0 | 2025-09-18T22:07:07.851625 |
| 2025-09-12 | 01405 | [17, 22, 24, 37, 42, 43] |      0 | 2025-09-18T22:07:07.851767 |
| 2025-09-10 | 01404 | [7, 10, 18, 20, 24, 36]  |      0 | 2025-09-18T22:07:07.851903 |
| 2025-09-07 | 01403 | [6, 29, 30, 39, 42, 44]  |      0 | 2025-09-18T22:07:07.852051 |
| 2025-09-05 | 01402 | [1, 10, 20, 22, 41, 43]  |      0 | 2025-09-18T22:07:07.852186 |
| 2025-09-03 | 01401 | [14, 21, 23, 28, 44, 45] |      0 | 2025-09-18T22:07:07.852318 |
| 2025-08-31 | 01400 | [3, 4, 14, 30, 32, 38]   |      0 | 2025-09-02 17:20:47.544748 |
| 2025-08-29 | 01399 | [2, 4, 10, 24, 35, 36]   |      0 | 2025-08-30 10:11:45.760729 |
| 2025-08-27 | 01398 | [3, 11, 18, 39, 40, 42]  |      0 | 2025-08-30 10:11:45.760827 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     187 | 2.22 |     |       21 |     181 | 2.14 |     | 41       | 189     | 2.24 |
|        2 |     177 | 2.1  |     |       22 |     200 | 2.37 |     | 42       | 178     | 2.11 |
|        3 |     172 | 2.04 |     |       23 |     187 | 2.22 |     | 43       | 173     | 2.05 |
|        4 |     198 | 2.35 |     |       24 |     210 | 2.49 |     | 44       | 204     | 2.42 |
|        5 |     198 | 2.35 |     |       25 |     193 | 2.29 |     | 45       | 185     | 2.19 |
|        6 |     191 | 2.26 |     |       26 |     186 | 2.2  |     |          |         |      |
|        7 |     203 | 2.4  |     |       27 |     194 | 2.3  |     |          |         |      |
|        8 |     186 | 2.2  |     |       28 |     196 | 2.32 |     |          |         |      |
|        9 |     181 | 2.14 |     |       29 |     189 | 2.24 |     |          |         |      |
|       10 |     208 | 2.46 |     |       30 |     198 | 2.35 |     |          |         |      |
|       11 |     194 | 2.3  |     |       31 |     184 | 2.18 |     |          |         |      |
|       12 |     171 | 2.03 |     |       32 |     179 | 2.12 |     |          |         |      |
|       13 |     193 | 2.29 |     |       33 |     187 | 2.22 |     |          |         |      |
|       14 |     182 | 2.16 |     |       34 |     186 | 2.2  |     |          |         |      |
|       15 |     173 | 2.05 |     |       35 |     192 | 2.27 |     |          |         |      |
|       16 |     189 | 2.24 |     |       36 |     173 | 2.05 |     |          |         |      |
|       17 |     169 | 2    |     |       37 |     207 | 2.45 |     |          |         |      |
|       18 |     184 | 2.18 |     |       38 |     160 | 1.9  |     |          |         |      |
|       19 |     207 | 2.45 |     |       39 |     174 | 2.06 |     |          |         |      |
|       20 |     196 | 2.32 |     |       40 |     178 | 2.11 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 2.56 |     | 28       | 2       | 2.56 |
|        2 |       2 | 2.56 |     | 29       | 1       | 1.28 |
|        3 |       3 | 3.85 |     | 30       | 3       | 3.85 |
|        4 |       3 | 3.85 |     | 32       | 3       | 3.85 |
|        6 |       2 | 2.56 |     | 35       | 2       | 2.56 |
|        7 |       1 | 1.28 |     | 36       | 2       | 2.56 |
|        9 |       4 | 5.13 |     | 37       | 3       | 3.85 |
|       10 |       5 | 6.41 |     | 38       | 3       | 3.85 |
|       11 |       2 | 2.56 |     | 39       | 3       | 3.85 |
|       13 |       1 | 1.28 |     | 40       | 1       | 1.28 |
|       14 |       2 | 2.56 |     | 41       | 1       | 1.28 |
|       17 |       1 | 1.28 |     | 42       | 4       | 5.13 |
|       18 |       2 | 2.56 |     | 43       | 3       | 3.85 |
|       20 |       3 | 3.85 |     | 44       | 2       | 2.56 |
|       21 |       1 | 1.28 |     | 45       | 2       | 2.56 |
|       22 |       2 | 2.56 |     |          |         |      |
|       23 |       2 | 2.56 |     |          |         |      |
|       24 |       3 | 3.85 |     |          |         |      |
|       25 |       1 | 1.28 |     |          |         |      |
|       27 |       1 | 1.28 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.92 |     |       23 |       2 | 1.28 |     | 44       | 3       | 1.92 |
|        2 |       3 | 1.92 |     |       24 |       6 | 3.85 |     | 45       | 5       | 3.21 |
|        3 |       5 | 3.21 |     |       25 |       1 | 0.64 |     |          |         |      |
|        4 |       3 | 1.92 |     |       26 |       6 | 3.85 |     |          |         |      |
|        5 |       3 | 1.92 |     |       27 |       4 | 2.56 |     |          |         |      |
|        6 |       3 | 1.92 |     |       28 |       4 | 2.56 |     |          |         |      |
|        7 |       1 | 0.64 |     |       29 |       5 | 3.21 |     |          |         |      |
|        9 |       5 | 3.21 |     |       30 |       6 | 3.85 |     |          |         |      |
|       10 |       6 | 3.85 |     |       31 |       3 | 1.92 |     |          |         |      |
|       11 |       4 | 2.56 |     |       32 |       4 | 2.56 |     |          |         |      |
|       12 |       2 | 1.28 |     |       34 |       3 | 1.92 |     |          |         |      |
|       13 |       3 | 1.92 |     |       35 |       5 | 3.21 |     |          |         |      |
|       14 |       5 | 3.21 |     |       36 |       4 | 2.56 |     |          |         |      |
|       15 |       2 | 1.28 |     |       37 |       6 | 3.85 |     |          |         |      |
|       16 |       1 | 0.64 |     |       38 |       6 | 3.85 |     |          |         |      |
|       17 |       2 | 1.28 |     |       39 |       5 | 3.21 |     |          |         |      |
|       18 |       3 | 1.92 |     |       40 |       1 | 0.64 |     |          |         |      |
|       20 |       6 | 3.85 |     |       41 |       1 | 0.64 |     |          |         |      |
|       21 |       2 | 1.28 |     |       42 |       6 | 3.85 |     |          |         |      |
|       22 |       3 | 1.92 |     |       43 |       5 | 3.21 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.71 |     |       21 |       5 | 2.14 |     | 41       | 4       | 1.71 |
|        2 |       4 | 1.71 |     |       22 |       7 | 2.99 |     | 42       | 8       | 3.42 |
|        3 |       5 | 2.14 |     |       23 |       4 | 1.71 |     | 43       | 6       | 2.56 |
|        4 |       3 | 1.28 |     |       24 |       8 | 3.42 |     | 44       | 5       | 2.14 |
|        5 |       4 | 1.71 |     |       25 |       2 | 0.85 |     | 45       | 10      | 4.27 |
|        6 |       4 | 1.71 |     |       26 |      10 | 4.27 |     |          |         |      |
|        7 |       4 | 1.71 |     |       27 |       6 | 2.56 |     |          |         |      |
|        8 |       4 | 1.71 |     |       28 |       7 | 2.99 |     |          |         |      |
|        9 |       9 | 3.85 |     |       29 |       8 | 3.42 |     |          |         |      |
|       10 |       8 | 3.42 |     |       30 |       8 | 3.42 |     |          |         |      |
|       11 |       6 | 2.56 |     |       31 |       3 | 1.28 |     |          |         |      |
|       12 |       3 | 1.28 |     |       32 |       5 | 2.14 |     |          |         |      |
|       13 |       4 | 1.71 |     |       33 |       1 | 0.43 |     |          |         |      |
|       14 |       8 | 3.42 |     |       34 |       5 | 2.14 |     |          |         |      |
|       15 |       2 | 0.85 |     |       35 |       7 | 2.99 |     |          |         |      |
|       16 |       2 | 0.85 |     |       36 |       6 | 2.56 |     |          |         |      |
|       17 |       3 | 1.28 |     |       37 |       6 | 2.56 |     |          |         |      |
|       18 |       4 | 1.71 |     |       38 |       6 | 2.56 |     |          |         |      |
|       19 |       1 | 0.43 |     |       39 |       6 | 2.56 |     |          |         |      |
|       20 |       8 | 3.42 |     |       40 |       1 | 0.43 |     |          |         |      |



### ⚖️ [6/45] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 493        | 35.04     |
| 4:2                  | 335        | 23.81     |
| 2:4                  | 307        | 21.82     |
| 5:1                  | 129        | 9.17      |
| 1:5                  | 108        | 7.68      |
| 6:0                  | 21         | 1.49      |
| 0:6                  | 14         | 1.00      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 5          | 38.46     |
| 1:5                  | 3          | 23.08     |
| 2:4                  | 3          | 23.08     |
| 5:1                  | 2          | 15.38     |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 11         | 42.31     |
| 2:4                  | 6          | 23.08     |
| 1:5                  | 4          | 15.38     |
| 5:1                  | 3          | 11.54     |
| 4:2                  | 2          | 7.69      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 16         | 41.03     |
| 2:4                  | 10         | 25.64     |
| 1:5                  | 5          | 12.82     |
| 4:2                  | 4          | 10.26     |
| 5:1                  | 3          | 7.69      |
| 6:0                  | 1          | 2.56      |


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
pip install -i https://test.pypi.org/simple/ vietlott-data==0.1.4
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

