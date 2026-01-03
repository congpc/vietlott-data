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
| Power 655 |          1273 | 2017-08-01   | 2026-01-01 |            1273 | 00001      | 01289       |
| Power 645 |          1437 | 2016-07-20   | 2026-01-02 |            1437 | 00001      | 01453       |
| Power 535 |           116 | 2025-06-29   | 2026-01-02 |             230 | 00001      | 00376       |
| Keno      |           353 | 2022-12-04   | 2026-01-03 |           46134 | #0110271   | #0265443    |
| 3D        |           992 | 2019-04-22   | 2025-10-20 |             992 | 00001      | 00992       |
| 3D Pro    |           638 | 2021-09-14   | 2025-10-18 |             638 | 00001      | 00638       |
| Bingo18   |           293 | 2024-12-03   | 2025-09-30 |           46246 | 0083123    | 0130917     |

## 🔮 Prediction Models 6/55

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                      | predicted               |
|:-----------|:----------------------------|:------------------------|
| 2022-12-01 | [11, 14, 29, 31, 52, 54, 7] | [54, 29, 49, 14, 7, 11] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2026-01-01 | 01289 | [5, 16, 29, 33, 39, 42, 54]  |      0 | 2026-01-03 12:46:36.077379 |
| 2025-12-30 | 01288 | [11, 30, 35, 41, 48, 55, 38] |      0 | 2026-01-03 12:46:36.077545 |
| 2025-12-27 | 01287 | [16, 21, 30, 37, 39, 40, 13] |      0 | 2026-01-03 12:46:36.077706 |
| 2025-12-25 | 01286 | [4, 6, 32, 37, 40, 48, 38]   |      0 | 2026-01-03 12:46:36.077858 |
| 2025-12-23 | 01285 | [2, 10, 16, 25, 32, 38, 3]   |      0 | 2026-01-03 12:46:36.078008 |
| 2025-12-20 | 01284 | [22, 32, 33, 35, 40, 41, 23] |      0 | 2026-01-03 12:46:36.078162 |
| 2025-12-18 | 01283 | [12, 14, 29, 30, 39, 55, 50] |      0 | 2026-01-03 12:46:36.078308 |
| 2025-12-16 | 01282 | [7, 36, 37, 38, 52, 55, 46]  |      0 | 2026-01-03 12:46:36.078454 |
| 2025-12-13 | 01281 | [5, 8, 12, 18, 20, 38, 52]   |      1 | 2026-01-03 12:46:35.865091 |
| 2025-12-11 | 01280 | [9, 13, 21, 45, 48, 55, 38]  |      1 | 2026-01-03 12:46:35.865308 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     172 | 1.93 |     |       21 |     157 | 1.76 |     | 41       | 189     | 2.12 |
|        2 |     148 | 1.66 |     |       22 |     182 | 2.04 |     | 42       | 166     | 1.86 |
|        3 |     172 | 1.93 |     |       23 |     173 | 1.94 |     | 43       | 183     | 2.05 |
|        4 |     135 | 1.52 |     |       24 |     166 | 1.86 |     | 44       | 169     | 1.9  |
|        5 |     164 | 1.84 |     |       25 |     143 | 1.6  |     | 45       | 162     | 1.82 |
|        6 |     137 | 1.54 |     |       26 |     150 | 1.68 |     | 46       | 166     | 1.86 |
|        7 |     139 | 1.56 |     |       27 |     149 | 1.67 |     | 47       | 161     | 1.81 |
|        8 |     173 | 1.94 |     |       28 |     141 | 1.58 |     | 48       | 174     | 1.95 |
|        9 |     179 | 2.01 |     |       29 |     170 | 1.91 |     | 49       | 161     | 1.81 |
|       10 |     152 | 1.71 |     |       30 |     145 | 1.63 |     | 50       | 162     | 1.82 |
|       11 |     166 | 1.86 |     |       31 |     168 | 1.89 |     | 51       | 184     | 2.07 |
|       12 |     169 | 1.9  |     |       32 |     168 | 1.89 |     | 52       | 168     | 1.89 |
|       13 |     154 | 1.73 |     |       33 |     163 | 1.83 |     | 53       | 170     | 1.91 |
|       14 |     162 | 1.82 |     |       34 |     182 | 2.04 |     | 54       | 151     | 1.69 |
|       15 |     151 | 1.69 |     |       35 |     160 | 1.8  |     | 55       | 162     | 1.82 |
|       16 |     154 | 1.73 |     |       36 |     152 | 1.71 |     |          |         |      |
|       17 |     148 | 1.66 |     |       37 |     149 | 1.67 |     |          |         |      |
|       18 |     164 | 1.84 |     |       38 |     157 | 1.76 |     |          |         |      |
|       19 |     163 | 1.83 |     |       39 |     156 | 1.75 |     |          |         |      |
|       20 |     171 | 1.92 |     |       40 |     178 | 2    |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        2 |       1 | 1.1 |     |       25 |       1 | 1.1  |     | 46       | 1       | 1.1 |
|        3 |       1 | 1.1 |     |       26 |       2 | 2.2  |     | 48       | 3       | 3.3 |
|        4 |       1 | 1.1 |     |       27 |       1 | 1.1  |     | 50       | 2       | 2.2 |
|        5 |       2 | 2.2 |     |       29 |       3 | 3.3  |     | 52       | 3       | 3.3 |
|        6 |       1 | 1.1 |     |       30 |       3 | 3.3  |     | 53       | 1       | 1.1 |
|        7 |       1 | 1.1 |     |       31 |       1 | 1.1  |     | 54       | 1       | 1.1 |
|        8 |       1 | 1.1 |     |       32 |       4 | 4.4  |     | 55       | 4       | 4.4 |
|        9 |       1 | 1.1 |     |       33 |       3 | 3.3  |     |          |         |     |
|       10 |       2 | 2.2 |     |       34 |       1 | 1.1  |     |          |         |     |
|       11 |       1 | 1.1 |     |       35 |       2 | 2.2  |     |          |         |     |
|       12 |       3 | 3.3 |     |       36 |       1 | 1.1  |     |          |         |     |
|       13 |       2 | 2.2 |     |       37 |       4 | 4.4  |     |          |         |     |
|       14 |       3 | 3.3 |     |       38 |       6 | 6.59 |     |          |         |     |
|       15 |       1 | 1.1 |     |       39 |       3 | 3.3  |     |          |         |     |
|       16 |       3 | 3.3 |     |       40 |       3 | 3.3  |     |          |         |     |
|       18 |       1 | 1.1 |     |       41 |       2 | 2.2  |     |          |         |     |
|       20 |       1 | 1.1 |     |       42 |       2 | 2.2  |     |          |         |     |
|       21 |       3 | 3.3 |     |       43 |       1 | 1.1  |     |          |         |     |
|       22 |       1 | 1.1 |     |       44 |       1 | 1.1  |     |          |         |     |
|       23 |       1 | 1.1 |     |       45 |       1 | 1.1  |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        2 |       1 | 0.89 |     |       24 |       2 | 1.79 |     | 44       | 1       | 0.89 |
|        3 |       1 | 0.89 |     |       25 |       1 | 0.89 |     | 45       | 1       | 0.89 |
|        4 |       3 | 2.68 |     |       26 |       2 | 1.79 |     | 46       | 1       | 0.89 |
|        5 |       3 | 2.68 |     |       27 |       2 | 1.79 |     | 48       | 4       | 3.57 |
|        6 |       1 | 0.89 |     |       28 |       1 | 0.89 |     | 50       | 2       | 1.79 |
|        7 |       1 | 0.89 |     |       29 |       3 | 2.68 |     | 51       | 1       | 0.89 |
|        8 |       1 | 0.89 |     |       30 |       3 | 2.68 |     | 52       | 3       | 2.68 |
|        9 |       2 | 1.79 |     |       31 |       1 | 0.89 |     | 53       | 1       | 0.89 |
|       10 |       4 | 3.57 |     |       32 |       4 | 3.57 |     | 54       | 2       | 1.79 |
|       11 |       2 | 1.79 |     |       33 |       3 | 2.68 |     | 55       | 4       | 3.57 |
|       12 |       3 | 2.68 |     |       34 |       1 | 0.89 |     |          |         |      |
|       13 |       2 | 1.79 |     |       35 |       3 | 2.68 |     |          |         |      |
|       14 |       3 | 2.68 |     |       36 |       2 | 1.79 |     |          |         |      |
|       15 |       1 | 0.89 |     |       37 |       4 | 3.57 |     |          |         |      |
|       16 |       4 | 3.57 |     |       38 |       7 | 6.25 |     |          |         |      |
|       18 |       1 | 0.89 |     |       39 |       3 | 2.68 |     |          |         |      |
|       20 |       3 | 2.68 |     |       40 |       4 | 3.57 |     |          |         |      |
|       21 |       3 | 2.68 |     |       41 |       2 | 1.79 |     |          |         |      |
|       22 |       1 | 0.89 |     |       42 |       2 | 1.79 |     |          |         |      |
|       23 |       1 | 0.89 |     |       43 |       1 | 0.89 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        2 |       1 | 0.65 |     |       23 |       1 | 0.65 |     | 43       | 4       | 2.6  |
|        3 |       2 | 1.3  |     |       24 |       3 | 1.95 |     | 44       | 2       | 1.3  |
|        4 |       3 | 1.95 |     |       25 |       2 | 1.3  |     | 45       | 3       | 1.95 |
|        5 |       4 | 2.6  |     |       26 |       5 | 3.25 |     | 46       | 2       | 1.3  |
|        6 |       1 | 0.65 |     |       27 |       3 | 1.95 |     | 48       | 4       | 2.6  |
|        7 |       3 | 1.95 |     |       28 |       1 | 0.65 |     | 50       | 3       | 1.95 |
|        8 |       2 | 1.3  |     |       29 |       4 | 2.6  |     | 51       | 1       | 0.65 |
|        9 |       3 | 1.95 |     |       30 |       3 | 1.95 |     | 52       | 3       | 1.95 |
|       10 |       4 | 2.6  |     |       31 |       1 | 0.65 |     | 53       | 1       | 0.65 |
|       11 |       3 | 1.95 |     |       32 |       4 | 2.6  |     | 54       | 2       | 1.3  |
|       12 |       4 | 2.6  |     |       33 |       3 | 1.95 |     | 55       | 5       | 3.25 |
|       13 |       2 | 1.3  |     |       34 |       1 | 0.65 |     |          |         |      |
|       14 |       4 | 2.6  |     |       35 |       4 | 2.6  |     |          |         |      |
|       15 |       2 | 1.3  |     |       36 |       3 | 1.95 |     |          |         |      |
|       16 |       6 | 3.9  |     |       37 |       6 | 3.9  |     |          |         |      |
|       18 |       1 | 0.65 |     |       38 |       8 | 5.19 |     |          |         |      |
|       19 |       2 | 1.3  |     |       39 |       4 | 2.6  |     |          |         |      |
|       20 |       3 | 1.95 |     |       40 |       5 | 3.25 |     |          |         |      |
|       21 |       5 | 3.25 |     |       41 |       2 | 1.3  |     |          |         |      |
|       22 |       3 | 1.95 |     |       42 |       3 | 1.95 |     |          |         |      |



### ⚖️ [6/55] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 429        | 33.70     |
| 2:4                  | 314        | 24.67     |
| 4:2                  | 301        | 23.64     |
| 5:1                  | 119        | 9.35      |
| 1:5                  | 83         | 6.52      |
| 6:0                  | 20         | 1.57      |
| 0:6                  | 7          | 0.55      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 5          | 38.46     |
| 1:5                  | 4          | 30.77     |
| 4:2                  | 3          | 23.08     |
| 5:1                  | 1          | 7.69      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 6          | 37.50     |
| 1:5                  | 6          | 37.50     |
| 4:2                  | 3          | 18.75     |
| 5:1                  | 1          | 6.25      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 9          | 40.91     |
| 1:5                  | 6          | 27.27     |
| 4:2                  | 5          | 22.73     |
| 5:1                  | 2          | 9.09      |


## 🔮 Prediction Models 6/45

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

No significant matches found in backtest period.



## 📈 Power 6/45 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                   |   page | process_time               |
|:-----------|------:|:-------------------------|-------:|:---------------------------|
| 2026-01-02 | 01453 | [7, 18, 22, 32, 37, 38]  |      0 | 2026-01-03T12:46:40.256599 |
| 2025-12-31 | 01452 | [1, 25, 35, 36, 37, 45]  |      0 | 2026-01-03T12:46:40.256800 |
| 2025-12-28 | 01451 | [1, 2, 7, 16, 31, 37]    |      0 | 2026-01-03T12:46:40.256953 |
| 2025-12-26 | 01450 | [4, 6, 16, 25, 27, 40]   |      0 | 2026-01-03T12:46:40.257112 |
| 2025-12-24 | 01449 | [15, 19, 31, 35, 43, 45] |      0 | 2026-01-03T12:46:40.257255 |
| 2025-12-21 | 01448 | [6, 9, 12, 18, 29, 43]   |      0 | 2026-01-03T12:46:40.257394 |
| 2025-12-19 | 01447 | [1, 21, 36, 42, 43, 44]  |      0 | 2026-01-03T12:46:40.257535 |
| 2025-12-17 | 01446 | [5, 14, 24, 38, 41, 43]  |      0 | 2026-01-03T12:46:40.257685 |
| 2025-12-14 | 01445 | [8, 11, 13, 16, 28, 32]  |      1 | 2026-01-03T12:46:40.695280 |
| 2025-12-12 | 01444 | [3, 7, 13, 17, 38, 44]   |      1 | 2026-01-03T12:46:40.695432 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     192 | 2.23 |     |       21 |     183 | 2.12 |     | 41       | 192     | 2.23 |
|        2 |     181 | 2.1  |     |       22 |     203 | 2.35 |     | 42       | 182     | 2.11 |
|        3 |     176 | 2.04 |     |       23 |     192 | 2.23 |     | 43       | 180     | 2.09 |
|        4 |     202 | 2.34 |     |       24 |     211 | 2.45 |     | 44       | 206     | 2.39 |
|        5 |     203 | 2.35 |     |       25 |     197 | 2.28 |     | 45       | 187     | 2.17 |
|        6 |     197 | 2.28 |     |       26 |     190 | 2.2  |     |          |         |      |
|        7 |     209 | 2.42 |     |       27 |     196 | 2.27 |     |          |         |      |
|        8 |     190 | 2.2  |     |       28 |     204 | 2.37 |     |          |         |      |
|        9 |     183 | 2.12 |     |       29 |     194 | 2.25 |     |          |         |      |
|       10 |     210 | 2.44 |     |       30 |     201 | 2.33 |     |          |         |      |
|       11 |     196 | 2.27 |     |       31 |     190 | 2.2  |     |          |         |      |
|       12 |     173 | 2.01 |     |       32 |     185 | 2.15 |     |          |         |      |
|       13 |     197 | 2.28 |     |       33 |     188 | 2.18 |     |          |         |      |
|       14 |     184 | 2.13 |     |       34 |     191 | 2.22 |     |          |         |      |
|       15 |     176 | 2.04 |     |       35 |     196 | 2.27 |     |          |         |      |
|       16 |     194 | 2.25 |     |       36 |     178 | 2.06 |     |          |         |      |
|       17 |     176 | 2.04 |     |       37 |     212 | 2.46 |     |          |         |      |
|       18 |     192 | 2.23 |     |       38 |     164 | 1.9  |     |          |         |      |
|       19 |     211 | 2.45 |     |       39 |     178 | 2.06 |     |          |         |      |
|       20 |     199 | 2.31 |     |       40 |     181 | 2.1  |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 5.13 |     | 23       | 2       | 2.56 |
|        2 |       2 | 2.56 |     | 24       | 1       | 1.28 |
|        3 |       1 | 1.28 |     | 25       | 2       | 2.56 |
|        4 |       1 | 1.28 |     | 27       | 1       | 1.28 |
|        5 |       2 | 2.56 |     | 28       | 2       | 2.56 |
|        6 |       2 | 2.56 |     | 29       | 3       | 3.85 |
|        7 |       4 | 5.13 |     | 30       | 1       | 1.28 |
|        8 |       1 | 1.28 |     | 31       | 2       | 2.56 |
|        9 |       1 | 1.28 |     | 32       | 2       | 2.56 |
|       11 |       1 | 1.28 |     | 35       | 2       | 2.56 |
|       12 |       1 | 1.28 |     | 36       | 3       | 3.85 |
|       13 |       2 | 2.56 |     | 37       | 4       | 5.13 |
|       14 |       1 | 1.28 |     | 38       | 3       | 3.85 |
|       15 |       1 | 1.28 |     | 40       | 1       | 1.28 |
|       16 |       3 | 3.85 |     | 41       | 1       | 1.28 |
|       17 |       1 | 1.28 |     | 42       | 2       | 2.56 |
|       18 |       3 | 3.85 |     | 43       | 6       | 7.69 |
|       19 |       2 | 2.56 |     | 44       | 2       | 2.56 |
|       21 |       1 | 1.28 |     | 45       | 2       | 2.56 |
|       22 |       2 | 2.56 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 4.17 |     |       22 |       2 | 2.08 |     | 43       | 6       | 6.25 |
|        2 |       3 | 3.12 |     |       23 |       4 | 4.17 |     | 44       | 2       | 2.08 |
|        3 |       1 | 1.04 |     |       24 |       1 | 1.04 |     | 45       | 2       | 2.08 |
|        4 |       1 | 1.04 |     |       25 |       2 | 2.08 |     |          |         |      |
|        5 |       2 | 2.08 |     |       26 |       1 | 1.04 |     |          |         |      |
|        6 |       2 | 2.08 |     |       27 |       1 | 1.04 |     |          |         |      |
|        7 |       5 | 5.21 |     |       28 |       2 | 2.08 |     |          |         |      |
|        8 |       2 | 2.08 |     |       29 |       3 | 3.12 |     |          |         |      |
|        9 |       2 | 2.08 |     |       30 |       2 | 2.08 |     |          |         |      |
|       11 |       1 | 1.04 |     |       31 |       3 | 3.12 |     |          |         |      |
|       12 |       1 | 1.04 |     |       32 |       2 | 2.08 |     |          |         |      |
|       13 |       3 | 3.12 |     |       34 |       2 | 2.08 |     |          |         |      |
|       14 |       1 | 1.04 |     |       35 |       2 | 2.08 |     |          |         |      |
|       15 |       2 | 2.08 |     |       36 |       3 | 3.12 |     |          |         |      |
|       16 |       3 | 3.12 |     |       37 |       4 | 4.17 |     |          |         |      |
|       17 |       2 | 2.08 |     |       38 |       3 | 3.12 |     |          |         |      |
|       18 |       3 | 3.12 |     |       39 |       1 | 1.04 |     |          |         |      |
|       19 |       2 | 2.08 |     |       40 |       1 | 1.04 |     |          |         |      |
|       20 |       1 | 1.04 |     |       41 |       2 | 2.08 |     |          |         |      |
|       21 |       1 | 1.04 |     |       42 |       3 | 3.12 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 3.62 |     |       21 |       1 | 0.72 |     | 42       | 4       | 2.9  |
|        2 |       3 | 2.17 |     |       22 |       3 | 2.17 |     | 43       | 7       | 5.07 |
|        3 |       1 | 0.72 |     |       23 |       5 | 3.62 |     | 44       | 2       | 1.45 |
|        4 |       3 | 2.17 |     |       24 |       1 | 0.72 |     | 45       | 2       | 1.45 |
|        5 |       4 | 2.9  |     |       25 |       4 | 2.9  |     |          |         |      |
|        6 |       3 | 2.17 |     |       26 |       3 | 2.17 |     |          |         |      |
|        7 |       5 | 3.62 |     |       27 |       1 | 0.72 |     |          |         |      |
|        8 |       3 | 2.17 |     |       28 |       5 | 3.62 |     |          |         |      |
|        9 |       2 | 1.45 |     |       29 |       4 | 2.9  |     |          |         |      |
|       10 |       2 | 1.45 |     |       30 |       2 | 1.45 |     |          |         |      |
|       11 |       2 | 1.45 |     |       31 |       4 | 2.9  |     |          |         |      |
|       12 |       1 | 0.72 |     |       32 |       4 | 2.9  |     |          |         |      |
|       13 |       3 | 2.17 |     |       34 |       4 | 2.9  |     |          |         |      |
|       14 |       2 | 1.45 |     |       35 |       2 | 1.45 |     |          |         |      |
|       15 |       3 | 2.17 |     |       36 |       3 | 2.17 |     |          |         |      |
|       16 |       5 | 3.62 |     |       37 |       5 | 3.62 |     |          |         |      |
|       17 |       4 | 2.9  |     |       38 |       3 | 2.17 |     |          |         |      |
|       18 |       6 | 4.35 |     |       39 |       3 | 2.17 |     |          |         |      |
|       19 |       2 | 1.45 |     |       40 |       2 | 1.45 |     |          |         |      |
|       20 |       3 | 2.17 |     |       41 |       2 | 1.45 |     |          |         |      |



### ⚖️ [6/45] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 500        | 34.79     |
| 4:2                  | 342        | 23.80     |
| 2:4                  | 318        | 22.13     |
| 5:1                  | 132        | 9.19      |
| 1:5                  | 108        | 7.52      |
| 6:0                  | 22         | 1.53      |
| 0:6                  | 15         | 1.04      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 4          | 30.77     |
| 4:2                  | 3          | 23.08     |
| 3:3                  | 3          | 23.08     |
| 5:1                  | 2          | 15.38     |
| 6:0                  | 1          | 7.69      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 5          | 31.25     |
| 3:3                  | 4          | 25.00     |
| 5:1                  | 3          | 18.75     |
| 4:2                  | 3          | 18.75     |
| 6:0                  | 1          | 6.25      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 8          | 34.78     |
| 3:3                  | 6          | 26.09     |
| 4:2                  | 4          | 17.39     |
| 5:1                  | 3          | 13.04     |
| 6:0                  | 1          | 4.35      |
| 0:6                  | 1          | 4.35      |


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

