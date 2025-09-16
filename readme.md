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
| Power 655 |          1237 | 2017-08-01   | 2025-09-02 |            1237 | 00001      | 01237       |
| Power 645 |          1400 | 2016-07-20   | 2025-08-31 |            1400 | 00001      | 01400       |
| Power 535 |            63 | 2025-06-29   | 2025-09-02 |             124 | 00001      | 00132       |
| Keno      |           318 | 2022-12-04   | 2025-08-30 |           41889 | #0110271   | #0250431    |
| 3D        |           971 | 2019-04-22   | 2025-09-01 |             971 | 00001      | 00971       |
| 3D Pro    |           618 | 2021-09-14   | 2025-09-02 |             618 | 00001      | 00618       |
| Bingo18   |           275 | 2024-12-03   | 2025-09-03 |           43436 | 0083123    | 0126625     |

## 🔮 Prediction Models 6/55

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                     | predicted               |
|:-----------|:---------------------------|:------------------------|
| 2022-07-02 | [6, 26, 39, 40, 46, 47, 2] | [26, 2, 39, 46, 47, 45] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                      |   page | process_time               |
|:-----------|------:|:----------------------------|-------:|:---------------------------|
| 2025-09-02 | 01237 | [9, 16, 22, 25, 30, 51, 43] |      0 | 2025-09-03 09:49:14.784413 |
| 2025-08-30 | 01236 | [2, 17, 19, 24, 30, 44, 34] |      0 | 2025-08-31 12:07:10.223130 |
| 2025-08-28 | 01235 | [6, 13, 28, 30, 35, 52, 50] |      0 | 2025-08-30 10:11:29.649921 |
| 2025-08-26 | 01234 | [22, 30, 38, 44, 48, 55, 5] |      0 | 2025-08-30 10:11:29.650069 |
| 2025-08-23 | 01233 | [1, 9, 26, 34, 44, 50, 52]  |      0 | 2025-08-25 14:42:48.767122 |
| 2025-08-21 | 01232 | [5, 9, 17, 35, 40, 41, 44]  |      0 | 2025-08-25 14:42:48.767269 |
| 2025-08-19 | 01231 | [1, 14, 31, 34, 36, 47, 45] |      0 | 2025-08-20 14:17:55.225324 |
| 2025-08-16 | 01230 | [14, 23, 32, 36, 47, 48, 5] |      0 | 2025-08-18 10:50:12.934699 |
| 2025-08-14 | 01229 | [6, 10, 17, 18, 32, 35, 53] |      0 | 2025-08-18 10:50:12.934740 |
| 2025-08-12 | 01228 | [1, 6, 24, 37, 40, 55, 10]  |      0 | 2025-08-13 14:39:19.796410 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     170 | 1.96 |     |       21 |     151 | 1.74 |     | 41       | 186     | 2.15 |
|        2 |     143 | 1.65 |     |       22 |     177 | 2.04 |     | 42       | 160     | 1.85 |
|        3 |     169 | 1.95 |     |       23 |     170 | 1.96 |     | 43       | 175     | 2.02 |
|        4 |     132 | 1.52 |     |       24 |     160 | 1.85 |     | 44       | 167     | 1.93 |
|        5 |     159 | 1.84 |     |       25 |     141 | 1.63 |     | 45       | 158     | 1.82 |
|        6 |     135 | 1.56 |     |       26 |     145 | 1.67 |     | 46       | 160     | 1.85 |
|        7 |     134 | 1.55 |     |       27 |     143 | 1.65 |     | 47       | 161     | 1.86 |
|        8 |     165 | 1.91 |     |       28 |     139 | 1.61 |     | 48       | 170     | 1.96 |
|        9 |     174 | 2.01 |     |       29 |     166 | 1.92 |     | 49       | 159     | 1.84 |
|       10 |     148 | 1.71 |     |       30 |     140 | 1.62 |     | 50       | 159     | 1.84 |
|       11 |     162 | 1.87 |     |       31 |     164 | 1.89 |     | 51       | 182     | 2.1  |
|       12 |     165 | 1.91 |     |       32 |     164 | 1.89 |     | 52       | 163     | 1.88 |
|       13 |     150 | 1.73 |     |       33 |     158 | 1.82 |     | 53       | 166     | 1.92 |
|       14 |     157 | 1.81 |     |       34 |     178 | 2.06 |     | 54       | 149     | 1.72 |
|       15 |     148 | 1.71 |     |       35 |     155 | 1.79 |     | 55       | 155     | 1.79 |
|       16 |     146 | 1.69 |     |       36 |     147 | 1.7  |     |          |         |      |
|       17 |     145 | 1.67 |     |       37 |     143 | 1.65 |     |          |         |      |
|       18 |     161 | 1.86 |     |       38 |     145 | 1.67 |     |          |         |      |
|       19 |     155 | 1.79 |     |       39 |     149 | 1.72 |     |          |         |      |
|       20 |     165 | 1.91 |     |       40 |     170 | 1.96 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 4.08 |     | 38       | 1       | 2.04 |
|        2 |       1 | 2.04 |     | 40       | 1       | 2.04 |
|        5 |       2 | 4.08 |     | 41       | 1       | 2.04 |
|        6 |       1 | 2.04 |     | 43       | 1       | 2.04 |
|        9 |       3 | 6.12 |     | 44       | 4       | 8.16 |
|       13 |       1 | 2.04 |     | 45       | 1       | 2.04 |
|       14 |       1 | 2.04 |     | 47       | 1       | 2.04 |
|       16 |       1 | 2.04 |     | 48       | 1       | 2.04 |
|       17 |       2 | 4.08 |     | 50       | 2       | 4.08 |
|       19 |       1 | 2.04 |     | 51       | 1       | 2.04 |
|       22 |       2 | 4.08 |     | 52       | 2       | 4.08 |
|       24 |       1 | 2.04 |     | 55       | 1       | 2.04 |
|       25 |       1 | 2.04 |     |          |         |      |
|       26 |       1 | 2.04 |     |          |         |      |
|       28 |       1 | 2.04 |     |          |         |      |
|       30 |       4 | 8.16 |     |          |         |      |
|       31 |       1 | 2.04 |     |          |         |      |
|       34 |       3 | 6.12 |     |          |         |      |
|       35 |       2 | 4.08 |     |          |         |      |
|       36 |       1 | 2.04 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 2.14 |     |       25 |       1 | 0.71 |     | 46       | 1       | 0.71 |
|        2 |       1 | 0.71 |     |       26 |       2 | 1.43 |     | 47       | 3       | 2.14 |
|        4 |       1 | 0.71 |     |       28 |       4 | 2.86 |     | 48       | 4       | 2.86 |
|        5 |       7 | 5    |     |       29 |       3 | 2.14 |     | 49       | 1       | 0.71 |
|        6 |       4 | 2.86 |     |       30 |       5 | 3.57 |     | 50       | 2       | 1.43 |
|        8 |       3 | 2.14 |     |       31 |       4 | 2.86 |     | 51       | 4       | 2.86 |
|        9 |       6 | 4.29 |     |       32 |       3 | 2.14 |     | 52       | 4       | 2.86 |
|       10 |       4 | 2.86 |     |       33 |       3 | 2.14 |     | 53       | 2       | 1.43 |
|       12 |       1 | 0.71 |     |       34 |       6 | 4.29 |     | 54       | 1       | 0.71 |
|       13 |       1 | 0.71 |     |       35 |       4 | 2.86 |     | 55       | 2       | 1.43 |
|       14 |       2 | 1.43 |     |       36 |       4 | 2.86 |     |          |         |      |
|       15 |       1 | 0.71 |     |       37 |       2 | 1.43 |     |          |         |      |
|       16 |       2 | 1.43 |     |       38 |       1 | 0.71 |     |          |         |      |
|       17 |       4 | 2.86 |     |       39 |       2 | 1.43 |     |          |         |      |
|       18 |       1 | 0.71 |     |       40 |       2 | 1.43 |     |          |         |      |
|       19 |       2 | 1.43 |     |       41 |       2 | 1.43 |     |          |         |      |
|       20 |       1 | 0.71 |     |       42 |       1 | 0.71 |     |          |         |      |
|       22 |       3 | 2.14 |     |       43 |       3 | 2.14 |     |          |         |      |
|       23 |       2 | 1.43 |     |       44 |       6 | 4.29 |     |          |         |      |
|       24 |       5 | 3.57 |     |       45 |       4 | 2.86 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.73 |     |       23 |       3 | 1.3  |     | 43       | 4       | 1.73 |
|        2 |       3 | 1.3  |     |       24 |       6 | 2.6  |     | 44       | 8       | 3.46 |
|        3 |       5 | 2.16 |     |       25 |       2 | 0.87 |     | 45       | 8       | 3.46 |
|        4 |       1 | 0.43 |     |       26 |       3 | 1.3  |     | 46       | 1       | 0.43 |
|        5 |       8 | 3.46 |     |       27 |       3 | 1.3  |     | 47       | 4       | 1.73 |
|        6 |       5 | 2.16 |     |       28 |       4 | 1.73 |     | 48       | 8       | 3.46 |
|        8 |       4 | 1.73 |     |       29 |       4 | 1.73 |     | 49       | 1       | 0.43 |
|        9 |       8 | 3.46 |     |       30 |       7 | 3.03 |     | 50       | 4       | 1.73 |
|       10 |       6 | 2.6  |     |       31 |       7 | 3.03 |     | 51       | 7       | 3.03 |
|       11 |       2 | 0.87 |     |       32 |       6 | 2.6  |     | 52       | 5       | 2.16 |
|       12 |       3 | 1.3  |     |       33 |       6 | 2.6  |     | 53       | 6       | 2.6  |
|       13 |       3 | 1.3  |     |       34 |       9 | 3.9  |     | 54       | 4       | 1.73 |
|       14 |       4 | 1.73 |     |       35 |       4 | 1.73 |     | 55       | 3       | 1.3  |
|       15 |       4 | 1.73 |     |       36 |       5 | 2.16 |     |          |         |      |
|       16 |       4 | 1.73 |     |       37 |       2 | 0.87 |     |          |         |      |
|       17 |       4 | 1.73 |     |       38 |       1 | 0.43 |     |          |         |      |
|       18 |       5 | 2.16 |     |       39 |       3 | 1.3  |     |          |         |      |
|       19 |       3 | 1.3  |     |       40 |       4 | 1.73 |     |          |         |      |
|       20 |       3 | 1.3  |     |       41 |       3 | 1.3  |     |          |         |      |
|       22 |       4 | 1.73 |     |       42 |       3 | 1.3  |     |          |         |      |



### ⚖️ [6/55] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 414        | 33.47     |
| 2:4                  | 310        | 25.06     |
| 4:2                  | 294        | 23.77     |
| 5:1                  | 115        | 9.30      |
| 1:5                  | 77         | 6.22      |
| 6:0                  | 20         | 1.62      |
| 0:6                  | 7          | 0.57      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 3          | 42.86     |
| 3:3                  | 2          | 28.57     |
| 1:5                  | 1          | 14.29     |
| 5:1                  | 1          | 14.29     |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 8          | 40.00     |
| 3:3                  | 6          | 30.00     |
| 4:2                  | 4          | 20.00     |
| 1:5                  | 1          | 5.00      |
| 5:1                  | 1          | 5.00      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 12         | 36.36     |
| 2:4                  | 9          | 27.27     |
| 4:2                  | 7          | 21.21     |
| 1:5                  | 3          | 9.09      |
| 5:1                  | 2          | 6.06      |


## 🔮 Prediction Models 6/45

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                   | predicted                |
|:-----------|:-------------------------|:-------------------------|
| 2023-03-03 | [10, 22, 26, 27, 33, 43] | [10, 22, 33, 26, 39, 27] |



## 📈 Power 6/45 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                   |   page | process_time               |
|:-----------|------:|:-------------------------|-------:|:---------------------------|
| 2025-08-31 | 01400 | [3, 4, 14, 30, 32, 38]   |      0 | 2025-09-02 17:20:47.544748 |
| 2025-08-29 | 01399 | [2, 4, 10, 24, 35, 36]   |      0 | 2025-08-30 10:11:45.760729 |
| 2025-08-27 | 01398 | [3, 11, 18, 39, 40, 42]  |      0 | 2025-08-30 10:11:45.760827 |
| 2025-08-24 | 01397 | [2, 9, 20, 28, 32, 43]   |      0 | 2025-08-25 14:42:55.038399 |
| 2025-08-22 | 01396 | [1, 9, 10, 13, 37, 39]   |      0 | 2025-08-25 14:42:55.038543 |
| 2025-08-20 | 01395 | [4, 9, 27, 32, 38, 42]   |      0 | 2025-08-25 14:42:55.038654 |
| 2025-08-17 | 01394 | [15, 24, 26, 29, 31, 42] |      0 | 2025-08-18 10:50:17.132683 |
| 2025-08-15 | 01393 | [5, 22, 27, 36, 43, 45]  |      0 | 2025-08-18 10:50:17.132735 |
| 2025-08-13 | 01392 | [10, 15, 28, 30, 35, 45] |      0 | 2025-08-14 14:53:45.734700 |
| 2025-08-10 | 01391 | [13, 21, 26, 28, 31, 35] |      0 | 2025-08-13 14:28:12.808613 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     186 | 2.21 |     |       21 |     180 | 2.14 |     | 41       | 188     | 2.24 |
|        2 |     177 | 2.11 |     |       22 |     198 | 2.36 |     | 42       | 176     | 2.1  |
|        3 |     171 | 2.04 |     |       23 |     185 | 2.2  |     | 43       | 171     | 2.04 |
|        4 |     198 | 2.36 |     |       24 |     208 | 2.48 |     | 44       | 202     | 2.4  |
|        5 |     198 | 2.36 |     |       25 |     192 | 2.29 |     | 45       | 183     | 2.18 |
|        6 |     189 | 2.25 |     |       26 |     186 | 2.21 |     |          |         |      |
|        7 |     202 | 2.4  |     |       27 |     194 | 2.31 |     |          |         |      |
|        8 |     186 | 2.21 |     |       28 |     195 | 2.32 |     |          |         |      |
|        9 |     180 | 2.14 |     |       29 |     188 | 2.24 |     |          |         |      |
|       10 |     205 | 2.44 |     |       30 |     196 | 2.33 |     |          |         |      |
|       11 |     193 | 2.3  |     |       31 |     184 | 2.19 |     |          |         |      |
|       12 |     171 | 2.04 |     |       32 |     179 | 2.13 |     |          |         |      |
|       13 |     193 | 2.3  |     |       33 |     187 | 2.23 |     |          |         |      |
|       14 |     181 | 2.15 |     |       34 |     186 | 2.21 |     |          |         |      |
|       15 |     173 | 2.06 |     |       35 |     191 | 2.27 |     |          |         |      |
|       16 |     189 | 2.25 |     |       36 |     172 | 2.05 |     |          |         |      |
|       17 |     168 | 2    |     |       37 |     205 | 2.44 |     |          |         |      |
|       18 |     183 | 2.18 |     |       38 |     159 | 1.89 |     |          |         |      |
|       19 |     207 | 2.46 |     |       39 |     173 | 2.06 |     |          |         |      |
|       20 |     194 | 2.31 |     |       40 |     178 | 2.12 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 2.38 |     | 35       | 1       | 2.38 |
|        2 |       2 | 4.76 |     | 36       | 1       | 2.38 |
|        3 |       2 | 4.76 |     | 37       | 1       | 2.38 |
|        4 |       3 | 7.14 |     | 38       | 2       | 4.76 |
|        9 |       3 | 7.14 |     | 39       | 2       | 4.76 |
|       10 |       2 | 4.76 |     | 40       | 1       | 2.38 |
|       11 |       1 | 2.38 |     | 42       | 3       | 7.14 |
|       13 |       1 | 2.38 |     | 43       | 1       | 2.38 |
|       14 |       1 | 2.38 |     |          |         |      |
|       15 |       1 | 2.38 |     |          |         |      |
|       18 |       1 | 2.38 |     |          |         |      |
|       20 |       1 | 2.38 |     |          |         |      |
|       24 |       2 | 4.76 |     |          |         |      |
|       26 |       1 | 2.38 |     |          |         |      |
|       27 |       1 | 2.38 |     |          |         |      |
|       28 |       1 | 2.38 |     |          |         |      |
|       29 |       1 | 2.38 |     |          |         |      |
|       30 |       1 | 2.38 |     |          |         |      |
|       31 |       1 | 2.38 |     |          |         |      |
|       32 |       3 | 7.14 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.67 |     | 24       | 5       | 4.17 |
|        2 |       3 | 2.5  |     | 26       | 6       | 5.0  |
|        3 |       4 | 3.33 |     | 27       | 4       | 3.33 |
|        4 |       3 | 2.5  |     | 28       | 4       | 3.33 |
|        5 |       3 | 2.5  |     | 29       | 4       | 3.33 |
|        6 |       1 | 0.83 |     | 30       | 4       | 3.33 |
|        7 |       1 | 0.83 |     | 31       | 3       | 2.5  |
|        9 |       4 | 3.33 |     | 32       | 4       | 3.33 |
|       10 |       3 | 2.5  |     | 34       | 3       | 2.5  |
|       11 |       3 | 2.5  |     | 35       | 4       | 3.33 |
|       12 |       2 | 1.67 |     | 36       | 3       | 2.5  |
|       13 |       3 | 2.5  |     | 37       | 4       | 3.33 |
|       14 |       4 | 3.33 |     | 38       | 5       | 4.17 |
|       15 |       2 | 1.67 |     | 39       | 4       | 3.33 |
|       16 |       1 | 0.83 |     | 40       | 1       | 0.83 |
|       17 |       1 | 0.83 |     | 42       | 5       | 4.17 |
|       18 |       2 | 1.67 |     | 43       | 3       | 2.5  |
|       20 |       4 | 3.33 |     | 44       | 1       | 0.83 |
|       21 |       1 | 0.83 |     | 45       | 4       | 3.33 |
|       22 |       2 | 1.67 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.52 |     |       21 |       4 | 2.02 |     | 41       | 4       | 2.02 |
|        2 |       4 | 2.02 |     |       22 |       5 | 2.53 |     | 42       | 6       | 3.03 |
|        3 |       4 | 2.02 |     |       23 |       3 | 1.52 |     | 43       | 4       | 2.02 |
|        4 |       3 | 1.52 |     |       24 |       7 | 3.54 |     | 44       | 3       | 1.52 |
|        5 |       4 | 2.02 |     |       25 |       1 | 0.51 |     | 45       | 8       | 4.04 |
|        6 |       2 | 1.01 |     |       26 |      11 | 5.56 |     |          |         |      |
|        7 |       3 | 1.52 |     |       27 |       6 | 3.03 |     |          |         |      |
|        8 |       4 | 2.02 |     |       28 |       6 | 3.03 |     |          |         |      |
|        9 |       8 | 4.04 |     |       29 |       7 | 3.54 |     |          |         |      |
|       10 |       5 | 2.53 |     |       30 |       6 | 3.03 |     |          |         |      |
|       11 |       5 | 2.53 |     |       31 |       3 | 1.52 |     |          |         |      |
|       12 |       3 | 1.52 |     |       32 |       5 | 2.53 |     |          |         |      |
|       13 |       4 | 2.02 |     |       33 |       1 | 0.51 |     |          |         |      |
|       14 |       7 | 3.54 |     |       34 |       5 | 2.53 |     |          |         |      |
|       15 |       2 | 1.01 |     |       35 |       6 | 3.03 |     |          |         |      |
|       16 |       2 | 1.01 |     |       36 |       6 | 3.03 |     |          |         |      |
|       17 |       2 | 1.01 |     |       37 |       4 | 2.02 |     |          |         |      |
|       18 |       3 | 1.52 |     |       38 |       5 | 2.53 |     |          |         |      |
|       19 |       2 | 1.01 |     |       39 |       5 | 2.53 |     |          |         |      |
|       20 |       6 | 3.03 |     |       40 |       1 | 0.51 |     |          |         |      |



### ⚖️ [6/45] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 489        | 34.93     |
| 4:2                  | 335        | 23.93     |
| 2:4                  | 306        | 21.86     |
| 5:1                  | 128        | 9.14      |
| 1:5                  | 107        | 7.64      |
| 6:0                  | 21         | 1.50      |
| 0:6                  | 14         | 1.00      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 1:5                  | 2          | 28.57     |
| 3:3                  | 2          | 28.57     |
| 2:4                  | 2          | 28.57     |
| 5:1                  | 1          | 14.29     |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 7          | 35.00     |
| 2:4                  | 6          | 30.00     |
| 1:5                  | 3          | 15.00     |
| 5:1                  | 2          | 10.00     |
| 4:2                  | 2          | 10.00     |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 13         | 39.39     |
| 2:4                  | 9          | 27.27     |
| 1:5                  | 4          | 12.12     |
| 4:2                  | 4          | 12.12     |
| 5:1                  | 2          | 6.06      |
| 6:0                  | 1          | 3.03      |


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

