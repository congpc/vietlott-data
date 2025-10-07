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
| Power 655 |          1251 | 2017-08-01   | 2025-10-04 |            1251 | 00001      | 01251       |
| Power 645 |          1414 | 2016-07-20   | 2025-10-03 |            1414 | 00001      | 01414       |
| Power 535 |            93 | 2025-06-29   | 2025-10-05 |             183 | 00001      | 00197       |
| Keno      |           343 | 2022-12-04   | 2025-09-30 |           44920 | #0110271   | #0254111    |
| 3D        |           985 | 2019-04-22   | 2025-10-03 |             985 | 00001      | 00985       |
| 3D Pro    |           632 | 2021-09-14   | 2025-10-04 |             632 | 00001      | 00632       |
| Bingo18   |           293 | 2024-12-03   | 2025-09-30 |           46246 | 0083123    | 0130917     |

## 🔮 Prediction Models 6/55

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                       | predicted                |
|:-----------|:-----------------------------|:-------------------------|
| 2023-10-21 | [11, 16, 24, 34, 47, 52, 15] | [15, 47, 49, 16, 24, 34] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-10-04 | 01251 | [22, 33, 35, 36, 38, 40, 7]  |      0 | 2025-10-05T17:04:48.001158 |
| 2025-10-02 | 01250 | [1, 2, 20, 24, 27, 42, 43]   |      0 | 2025-10-05T17:04:48.001330 |
| 2025-09-30 | 01249 | [17, 23, 34, 39, 46, 52, 8]  |      0 | 2025-09-30 19:22:07.239312 |
| 2025-09-27 | 01248 | [8, 13, 19, 24, 39, 46, 1]   |      0 | 2025-09-30 19:22:07.239405 |
| 2025-09-25 | 01247 | [5, 17, 30, 31, 38, 53, 8]   |      0 | 2025-09-30 19:22:07.239490 |
| 2025-09-23 | 01246 | [8, 18, 19, 34, 41, 46, 38]  |      0 | 2025-09-30 19:22:07.239573 |
| 2025-09-20 | 01245 | [8, 13, 14, 19, 36, 43, 30]  |      0 | 2025-09-21 07:37:04.165282 |
| 2025-09-18 | 01244 | [2, 3, 8, 27, 38, 55, 20]    |      0 | 2025-09-18 19:49:45.191045 |
| 2025-09-16 | 01243 | [17, 19, 28, 39, 43, 53, 33] |      0 | 2025-09-16 19:20:04.498817 |
| 2025-09-13 | 01242 | [2, 7, 15, 18, 24, 27, 45]   |      0 | 2025-09-13 18:44:39.730760 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     172 | 1.96 |     |       21 |     152 | 1.74 |     | 41       | 187     | 2.14 |
|        2 |     147 | 1.68 |     |       22 |     179 | 2.04 |     | 42       | 163     | 1.86 |
|        3 |     170 | 1.94 |     |       23 |     172 | 1.96 |     | 43       | 179     | 2.04 |
|        4 |     132 | 1.51 |     |       24 |     163 | 1.86 |     | 44       | 167     | 1.91 |
|        5 |     160 | 1.83 |     |       25 |     141 | 1.61 |     | 45       | 159     | 1.82 |
|        6 |     136 | 1.55 |     |       26 |     145 | 1.66 |     | 46       | 164     | 1.87 |
|        7 |     136 | 1.55 |     |       27 |     146 | 1.67 |     | 47       | 161     | 1.84 |
|        8 |     171 | 1.95 |     |       28 |     140 | 1.6  |     | 48       | 170     | 1.94 |
|        9 |     176 | 2.01 |     |       29 |     166 | 1.9  |     | 49       | 161     | 1.84 |
|       10 |     148 | 1.69 |     |       30 |     142 | 1.62 |     | 50       | 159     | 1.82 |
|       11 |     163 | 1.86 |     |       31 |     167 | 1.91 |     | 51       | 183     | 2.09 |
|       12 |     165 | 1.88 |     |       32 |     164 | 1.87 |     | 52       | 165     | 1.88 |
|       13 |     152 | 1.74 |     |       33 |     160 | 1.83 |     | 53       | 169     | 1.93 |
|       14 |     158 | 1.8  |     |       34 |     181 | 2.07 |     | 54       | 149     | 1.7  |
|       15 |     149 | 1.7  |     |       35 |     156 | 1.78 |     | 55       | 157     | 1.79 |
|       16 |     148 | 1.69 |     |       36 |     149 | 1.7  |     |          |         |      |
|       17 |     148 | 1.69 |     |       37 |     143 | 1.63 |     |          |         |      |
|       18 |     163 | 1.86 |     |       38 |     149 | 1.7  |     |          |         |      |
|       19 |     161 | 1.84 |     |       39 |     152 | 1.74 |     |          |         |      |
|       20 |     168 | 1.92 |     |       40 |     173 | 1.98 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |    % |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|
|        1 |       2 | 2.38 |     |       28 |       1 | 1.19 |
|        2 |       4 | 4.76 |     |       30 |       2 | 2.38 |
|        3 |       1 | 1.19 |     |       31 |       2 | 2.38 |
|        5 |       1 | 1.19 |     |       33 |       2 | 2.38 |
|        6 |       1 | 1.19 |     |       34 |       2 | 2.38 |
|        7 |       2 | 2.38 |     |       35 |       1 | 1.19 |
|        8 |       6 | 7.14 |     |       36 |       2 | 2.38 |
|       13 |       2 | 2.38 |     |       38 |       4 | 4.76 |
|       14 |       1 | 1.19 |     |       39 |       3 | 3.57 |
|       15 |       1 | 1.19 |     |       40 |       2 | 2.38 |
|       16 |       2 | 2.38 |     |       41 |       1 | 1.19 |
|       17 |       3 | 3.57 |     |       42 |       2 | 2.38 |
|       18 |       2 | 2.38 |     |       43 |       3 | 3.57 |
|       19 |       4 | 4.76 |     |       45 |       1 | 1.19 |
|       20 |       3 | 3.57 |     |       46 |       4 | 4.76 |
|       21 |       1 | 1.19 |     |       49 |       1 | 1.19 |
|       22 |       1 | 1.19 |     |       51 |       1 | 1.19 |
|       23 |       1 | 1.19 |     |       52 |       2 | 2.38 |
|       24 |       3 | 3.57 |     |       53 |       2 | 2.38 |
|       27 |       3 | 3.57 |     |       55 |       2 | 2.38 |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 2.86 |     |       23 |       3 | 1.71 |     | 44       | 4       | 2.29 |
|        2 |       5 | 2.86 |     |       24 |       5 | 2.86 |     | 45       | 2       | 1.14 |
|        3 |       1 | 0.57 |     |       25 |       1 | 0.57 |     | 46       | 4       | 2.29 |
|        5 |       5 | 2.86 |     |       26 |       1 | 0.57 |     | 47       | 2       | 1.14 |
|        6 |       4 | 2.29 |     |       27 |       3 | 1.71 |     | 48       | 2       | 1.14 |
|        7 |       2 | 1.14 |     |       28 |       2 | 1.14 |     | 49       | 2       | 1.14 |
|        8 |       6 | 3.43 |     |       30 |       6 | 3.43 |     | 50       | 2       | 1.14 |
|        9 |       6 | 3.43 |     |       31 |       4 | 2.29 |     | 51       | 3       | 1.71 |
|       10 |       2 | 1.14 |     |       32 |       2 | 1.14 |     | 52       | 4       | 2.29 |
|       11 |       1 | 0.57 |     |       33 |       2 | 1.14 |     | 53       | 4       | 2.29 |
|       13 |       3 | 1.71 |     |       34 |       6 | 3.43 |     | 55       | 4       | 2.29 |
|       14 |       3 | 1.71 |     |       35 |       4 | 2.29 |     |          |         |      |
|       15 |       1 | 0.57 |     |       36 |       5 | 2.86 |     |          |         |      |
|       16 |       4 | 2.29 |     |       37 |       1 | 0.57 |     |          |         |      |
|       17 |       6 | 3.43 |     |       38 |       5 | 2.86 |     |          |         |      |
|       18 |       3 | 1.71 |     |       39 |       3 | 1.71 |     |          |         |      |
|       19 |       8 | 4.57 |     |       40 |       5 | 2.86 |     |          |         |      |
|       20 |       3 | 1.71 |     |       41 |       2 | 1.14 |     |          |         |      |
|       21 |       1 | 0.57 |     |       42 |       3 | 1.71 |     |          |         |      |
|       22 |       4 | 2.29 |     |       43 |       6 | 3.43 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 1.88 |     |       21 |       1 | 0.38 |     | 41       | 4       | 1.5  |
|        2 |       6 | 2.26 |     |       22 |       5 | 1.88 |     | 42       | 5       | 1.88 |
|        3 |       2 | 0.75 |     |       23 |       4 | 1.5  |     | 43       | 7       | 2.63 |
|        4 |       1 | 0.38 |     |       24 |       8 | 3.01 |     | 44       | 7       | 2.63 |
|        5 |       8 | 3.01 |     |       25 |       1 | 0.38 |     | 45       | 6       | 2.26 |
|        6 |       5 | 1.88 |     |       26 |       3 | 1.13 |     | 46       | 5       | 1.88 |
|        7 |       2 | 0.75 |     |       27 |       3 | 1.13 |     | 47       | 3       | 1.13 |
|        8 |       9 | 3.38 |     |       28 |       5 | 1.88 |     | 48       | 6       | 2.26 |
|        9 |       8 | 3.01 |     |       29 |       3 | 1.13 |     | 49       | 3       | 1.13 |
|       10 |       4 | 1.5  |     |       30 |       8 | 3.01 |     | 50       | 2       | 0.75 |
|       11 |       1 | 0.38 |     |       31 |       8 | 3.01 |     | 51       | 6       | 2.26 |
|       12 |       2 | 0.75 |     |       32 |       4 | 1.5  |     | 52       | 7       | 2.63 |
|       13 |       4 | 1.5  |     |       33 |       7 | 2.63 |     | 53       | 7       | 2.63 |
|       14 |       3 | 1.13 |     |       34 |      11 | 4.14 |     | 54       | 2       | 0.75 |
|       15 |       2 | 0.75 |     |       35 |       5 | 1.88 |     | 55       | 4       | 1.5  |
|       16 |       4 | 1.5  |     |       36 |       7 | 2.63 |     |          |         |      |
|       17 |       7 | 2.63 |     |       37 |       2 | 0.75 |     |          |         |      |
|       18 |       5 | 1.88 |     |       38 |       5 | 1.88 |     |          |         |      |
|       19 |       8 | 3.01 |     |       39 |       6 | 2.26 |     |          |         |      |
|       20 |       4 | 1.5  |     |       40 |       6 | 2.26 |     |          |         |      |



### ⚖️ [6/55] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 420        | 33.57     |
| 2:4                  | 314        | 25.10     |
| 4:2                  | 296        | 23.66     |
| 5:1                  | 117        | 9.35      |
| 1:5                  | 77         | 6.16      |
| 6:0                  | 20         | 1.60      |
| 0:6                  | 7          | 0.56      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 6          | 50.00     |
| 2:4                  | 4          | 33.33     |
| 4:2                  | 1          | 8.33      |
| 5:1                  | 1          | 8.33      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 9          | 36.00     |
| 3:3                  | 9          | 36.00     |
| 4:2                  | 3          | 12.00     |
| 5:1                  | 3          | 12.00     |
| 1:5                  | 1          | 4.00      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 14         | 36.84     |
| 2:4                  | 13         | 34.21     |
| 4:2                  | 6          | 15.79     |
| 5:1                  | 3          | 7.89      |
| 1:5                  | 2          | 5.26      |


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
| 2025-10-03 | 01414 | [29, 31, 32, 33, 34, 35] |      0 | 2025-10-05T17:05:12.128384 |
| 2025-10-01 | 01413 | [3, 6, 7, 19, 30, 35]    |      0 | 2025-10-05T17:05:12.128562 |
| 2025-09-28 | 01412 | [8, 13, 18, 26, 36, 39]  |      0 | 2025-09-30 19:22:37.845940 |
| 2025-09-26 | 01411 | [12, 17, 19, 27, 28, 36] |      0 | 2025-09-30 19:22:37.846079 |
| 2025-09-24 | 01410 | [3, 5, 17, 31, 32, 40]   |      0 | 2025-09-30 19:22:37.846196 |
| 2025-09-21 | 01409 | [2, 3, 6, 21, 28, 38]    |      0 | 2025-09-30 19:22:37.846314 |
| 2025-09-19 | 01408 | [4, 6, 17, 18, 28, 41]   |      0 | 2025-09-19 21:19:53.906114 |
| 2025-09-17 | 01407 | [11, 23, 25, 35, 38, 45] |      0 | 2025-09-17 18:47:42.209975 |
| 2025-09-14 | 01406 | [3, 6, 9, 10, 30, 37]    |      0 | 2025-09-15 21:15:13.139917 |
| 2025-09-12 | 01405 | [17, 22, 24, 37, 42, 43] |      0 | 2025-09-12 21:43:38.569616 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     187 | 2.2  |     |       21 |     182 | 2.15 |     | 41       | 190     | 2.24 |
|        2 |     178 | 2.1  |     |       22 |     200 | 2.36 |     | 42       | 178     | 2.1  |
|        3 |     175 | 2.06 |     |       23 |     187 | 2.2  |     | 43       | 173     | 2.04 |
|        4 |     199 | 2.35 |     |       24 |     210 | 2.48 |     | 44       | 204     | 2.4  |
|        5 |     199 | 2.35 |     |       25 |     193 | 2.27 |     | 45       | 185     | 2.18 |
|        6 |     194 | 2.29 |     |       26 |     187 | 2.2  |     |          |         |      |
|        7 |     204 | 2.4  |     |       27 |     195 | 2.3  |     |          |         |      |
|        8 |     187 | 2.2  |     |       28 |     199 | 2.35 |     |          |         |      |
|        9 |     181 | 2.13 |     |       29 |     190 | 2.24 |     |          |         |      |
|       10 |     208 | 2.45 |     |       30 |     199 | 2.35 |     |          |         |      |
|       11 |     194 | 2.29 |     |       31 |     186 | 2.19 |     |          |         |      |
|       12 |     172 | 2.03 |     |       32 |     181 | 2.13 |     |          |         |      |
|       13 |     194 | 2.29 |     |       33 |     188 | 2.22 |     |          |         |      |
|       14 |     182 | 2.15 |     |       34 |     187 | 2.2  |     |          |         |      |
|       15 |     173 | 2.04 |     |       35 |     194 | 2.29 |     |          |         |      |
|       16 |     189 | 2.23 |     |       36 |     175 | 2.06 |     |          |         |      |
|       17 |     172 | 2.03 |     |       37 |     207 | 2.44 |     |          |         |      |
|       18 |     186 | 2.19 |     |       38 |     161 | 1.9  |     |          |         |      |
|       19 |     209 | 2.46 |     |       39 |     175 | 2.06 |     |          |         |      |
|       20 |     196 | 2.31 |     |       40 |     179 | 2.11 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        2 |       1 | 1.39 |     |       25 |       1 | 1.39 |     | 45       | 1       | 1.39 |
|        3 |       4 | 5.56 |     |       26 |       1 | 1.39 |     |          |         |      |
|        4 |       1 | 1.39 |     |       27 |       1 | 1.39 |     |          |         |      |
|        5 |       1 | 1.39 |     |       28 |       3 | 4.17 |     |          |         |      |
|        6 |       5 | 6.94 |     |       29 |       2 | 2.78 |     |          |         |      |
|        7 |       2 | 2.78 |     |       30 |       3 | 4.17 |     |          |         |      |
|        8 |       1 | 1.39 |     |       31 |       2 | 2.78 |     |          |         |      |
|        9 |       1 | 1.39 |     |       32 |       2 | 2.78 |     |          |         |      |
|       10 |       2 | 2.78 |     |       33 |       1 | 1.39 |     |          |         |      |
|       11 |       1 | 1.39 |     |       34 |       1 | 1.39 |     |          |         |      |
|       12 |       1 | 1.39 |     |       35 |       3 | 4.17 |     |          |         |      |
|       13 |       1 | 1.39 |     |       36 |       3 | 4.17 |     |          |         |      |
|       17 |       4 | 5.56 |     |       37 |       2 | 2.78 |     |          |         |      |
|       18 |       3 | 4.17 |     |       38 |       2 | 2.78 |     |          |         |      |
|       19 |       2 | 2.78 |     |       39 |       2 | 2.78 |     |          |         |      |
|       20 |       1 | 1.39 |     |       40 |       1 | 1.39 |     |          |         |      |
|       21 |       1 | 1.39 |     |       41 |       1 | 1.39 |     |          |         |      |
|       22 |       1 | 1.39 |     |       42 |       2 | 2.78 |     |          |         |      |
|       23 |       1 | 1.39 |     |       43 |       1 | 1.39 |     |          |         |      |
|       24 |       2 | 2.78 |     |       44 |       1 | 1.39 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.33 |     |       22 |       3 | 2    |     | 42       | 5       | 3.33 |
|        2 |       3 | 2    |     |       23 |       2 | 1.33 |     | 43       | 4       | 2.67 |
|        3 |       6 | 4    |     |       24 |       4 | 2.67 |     | 44       | 2       | 1.33 |
|        4 |       4 | 2.67 |     |       25 |       1 | 0.67 |     | 45       | 4       | 2.67 |
|        5 |       2 | 1.33 |     |       26 |       4 | 2.67 |     |          |         |      |
|        6 |       5 | 3.33 |     |       27 |       4 | 2.67 |     |          |         |      |
|        7 |       2 | 1.33 |     |       28 |       7 | 4.67 |     |          |         |      |
|        8 |       1 | 0.67 |     |       29 |       3 | 2    |     |          |         |      |
|        9 |       4 | 2.67 |     |       30 |       5 | 3.33 |     |          |         |      |
|       10 |       6 | 4    |     |       31 |       4 | 2.67 |     |          |         |      |
|       11 |       3 | 2    |     |       32 |       5 | 3.33 |     |          |         |      |
|       12 |       1 | 0.67 |     |       33 |       1 | 0.67 |     |          |         |      |
|       13 |       3 | 2    |     |       34 |       1 | 0.67 |     |          |         |      |
|       14 |       2 | 1.33 |     |       35 |       6 | 4    |     |          |         |      |
|       15 |       2 | 1.33 |     |       36 |       5 | 3.33 |     |          |         |      |
|       17 |       5 | 3.33 |     |       37 |       3 | 2    |     |          |         |      |
|       18 |       4 | 2.67 |     |       38 |       5 | 3.33 |     |          |         |      |
|       19 |       2 | 1.33 |     |       39 |       4 | 2.67 |     |          |         |      |
|       20 |       4 | 2.67 |     |       40 |       2 | 1.33 |     |          |         |      |
|       21 |       3 | 2    |     |       41 |       2 | 1.33 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.32 |     |       21 |       4 | 1.75 |     | 41       | 2       | 0.88 |
|        2 |       4 | 1.75 |     |       22 |       6 | 2.63 |     | 42       | 8       | 3.51 |
|        3 |       8 | 3.51 |     |       23 |       2 | 0.88 |     | 43       | 6       | 2.63 |
|        4 |       4 | 1.75 |     |       24 |       8 | 3.51 |     | 44       | 4       | 1.75 |
|        5 |       4 | 1.75 |     |       25 |       1 | 0.44 |     | 45       | 7       | 3.07 |
|        6 |       7 | 3.07 |     |       26 |       7 | 3.07 |     |          |         |      |
|        7 |       4 | 1.75 |     |       27 |       6 | 2.63 |     |          |         |      |
|        8 |       2 | 0.88 |     |       28 |       8 | 3.51 |     |          |         |      |
|        9 |       6 | 2.63 |     |       29 |       6 | 2.63 |     |          |         |      |
|       10 |       6 | 2.63 |     |       30 |       8 | 3.51 |     |          |         |      |
|       11 |       6 | 2.63 |     |       31 |       5 | 2.19 |     |          |         |      |
|       12 |       3 | 1.32 |     |       32 |       7 | 3.07 |     |          |         |      |
|       13 |       4 | 1.75 |     |       33 |       2 | 0.88 |     |          |         |      |
|       14 |       6 | 2.63 |     |       34 |       4 | 1.75 |     |          |         |      |
|       15 |       2 | 0.88 |     |       35 |       8 | 3.51 |     |          |         |      |
|       16 |       1 | 0.44 |     |       36 |       7 | 3.07 |     |          |         |      |
|       17 |       6 | 2.63 |     |       37 |       6 | 2.63 |     |          |         |      |
|       18 |       5 | 2.19 |     |       38 |       7 | 3.07 |     |          |         |      |
|       19 |       3 | 1.32 |     |       39 |       6 | 2.63 |     |          |         |      |
|       20 |       7 | 3.07 |     |       40 |       2 | 0.88 |     |          |         |      |



### ⚖️ [6/45] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 494        | 34.94     |
| 4:2                  | 338        | 23.90     |
| 2:4                  | 310        | 21.92     |
| 5:1                  | 129        | 9.12      |
| 1:5                  | 108        | 7.64      |
| 6:0                  | 21         | 1.49      |
| 0:6                  | 14         | 0.99      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 4          | 33.33     |
| 4:2                  | 3          | 25.00     |
| 3:3                  | 3          | 25.00     |
| 5:1                  | 1          | 8.33      |
| 1:5                  | 1          | 8.33      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 9          | 36.00     |
| 2:4                  | 6          | 24.00     |
| 4:2                  | 5          | 20.00     |
| 1:5                  | 3          | 12.00     |
| 5:1                  | 2          | 8.00      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 14         | 36.84     |
| 2:4                  | 11         | 28.95     |
| 4:2                  | 6          | 15.79     |
| 1:5                  | 4          | 10.53     |
| 5:1                  | 3          | 7.89      |


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

