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
| Power 655 |          1249 | 2017-08-01   | 2025-09-30 |            1249 | 00001      | 01249       |
| Power 645 |          1412 | 2016-07-20   | 2025-09-28 |            1412 | 00001      | 01412       |
| Power 535 |            88 | 2025-06-29   | 2025-09-30 |             173 | 00001      | 00187       |
| Keno      |           343 | 2022-12-04   | 2025-09-30 |           44920 | #0110271   | #0254111    |
| 3D        |           983 | 2019-04-22   | 2025-09-29 |             983 | 00001      | 00983       |
| 3D Pro    |           630 | 2021-09-14   | 2025-09-30 |             630 | 00001      | 00630       |
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
| 2021-04-22 | [5, 11, 17, 25, 39, 48, 22]  | [17, 11, 22, 48, 25, 16] |
| 2019-06-06 | [10, 13, 30, 36, 51, 54, 16] | [51, 36, 10, 16, 47, 30] |
| 2018-04-05 | [7, 9, 17, 25, 31, 32, 6]    | [6, 25, 7, 49, 32, 9]    |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-09-30 | 01249 | [17, 23, 34, 39, 46, 52, 8]  |      0 | 2025-09-30T19:22:07.239312 |
| 2025-09-27 | 01248 | [8, 13, 19, 24, 39, 46, 1]   |      0 | 2025-09-30T19:22:07.239405 |
| 2025-09-25 | 01247 | [5, 17, 30, 31, 38, 53, 8]   |      0 | 2025-09-30T19:22:07.239490 |
| 2025-09-23 | 01246 | [8, 18, 19, 34, 41, 46, 38]  |      0 | 2025-09-30T19:22:07.239573 |
| 2025-09-20 | 01245 | [8, 13, 14, 19, 36, 43, 30]  |      0 | 2025-09-21 07:37:04.165282 |
| 2025-09-18 | 01244 | [2, 3, 8, 27, 38, 55, 20]    |      0 | 2025-09-18 19:49:45.191045 |
| 2025-09-16 | 01243 | [17, 19, 28, 39, 43, 53, 33] |      0 | 2025-09-16 19:20:04.498817 |
| 2025-09-13 | 01242 | [2, 7, 15, 18, 24, 27, 45]   |      0 | 2025-09-13 18:44:39.730760 |
| 2025-09-11 | 01241 | [6, 16, 46, 49, 51, 55, 42]  |      0 | 2025-09-12 21:43:12.873808 |
| 2025-09-09 | 01240 | [16, 20, 21, 31, 40, 52, 2]  |      0 | 2025-09-12 21:43:12.873917 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     171 | 1.96 |     |       21 |     152 | 1.74 |     | 41       | 187     | 2.14 |
|        2 |     146 | 1.67 |     |       22 |     178 | 2.04 |     | 42       | 162     | 1.85 |
|        3 |     170 | 1.94 |     |       23 |     172 | 1.97 |     | 43       | 178     | 2.04 |
|        4 |     132 | 1.51 |     |       24 |     162 | 1.85 |     | 44       | 167     | 1.91 |
|        5 |     160 | 1.83 |     |       25 |     141 | 1.61 |     | 45       | 159     | 1.82 |
|        6 |     136 | 1.56 |     |       26 |     145 | 1.66 |     | 46       | 164     | 1.88 |
|        7 |     135 | 1.54 |     |       27 |     145 | 1.66 |     | 47       | 161     | 1.84 |
|        8 |     171 | 1.96 |     |       28 |     140 | 1.6  |     | 48       | 170     | 1.94 |
|        9 |     176 | 2.01 |     |       29 |     166 | 1.9  |     | 49       | 161     | 1.84 |
|       10 |     148 | 1.69 |     |       30 |     142 | 1.62 |     | 50       | 159     | 1.82 |
|       11 |     163 | 1.86 |     |       31 |     167 | 1.91 |     | 51       | 183     | 2.09 |
|       12 |     165 | 1.89 |     |       32 |     164 | 1.88 |     | 52       | 165     | 1.89 |
|       13 |     152 | 1.74 |     |       33 |     159 | 1.82 |     | 53       | 169     | 1.93 |
|       14 |     158 | 1.81 |     |       34 |     181 | 2.07 |     | 54       | 149     | 1.7  |
|       15 |     149 | 1.7  |     |       35 |     155 | 1.77 |     | 55       | 157     | 1.8  |
|       16 |     148 | 1.69 |     |       36 |     148 | 1.69 |     |          |         |      |
|       17 |     148 | 1.69 |     |       37 |     143 | 1.64 |     |          |         |      |
|       18 |     163 | 1.86 |     |       38 |     148 | 1.69 |     |          |         |      |
|       19 |     161 | 1.84 |     |       39 |     152 | 1.74 |     |          |         |      |
|       20 |     167 | 1.91 |     |       40 |     172 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       1 | 1.1  |     |       24 |       2 | 2.2 |     | 53       | 3       | 3.3 |
|        2 |       3 | 3.3  |     |       25 |       1 | 1.1 |     | 55       | 2       | 2.2 |
|        3 |       1 | 1.1  |     |       27 |       2 | 2.2 |     |          |         |     |
|        5 |       1 | 1.1  |     |       28 |       1 | 1.1 |     |          |         |     |
|        6 |       1 | 1.1  |     |       30 |       3 | 3.3 |     |          |         |     |
|        7 |       1 | 1.1  |     |       31 |       3 | 3.3 |     |          |         |     |
|        8 |       6 | 6.59 |     |       33 |       1 | 1.1 |     |          |         |     |
|        9 |       3 | 3.3  |     |       34 |       3 | 3.3 |     |          |         |     |
|       11 |       1 | 1.1  |     |       36 |       1 | 1.1 |     |          |         |     |
|       13 |       2 | 2.2  |     |       38 |       3 | 3.3 |     |          |         |     |
|       14 |       1 | 1.1  |     |       39 |       3 | 3.3 |     |          |         |     |
|       15 |       1 | 1.1  |     |       40 |       2 | 2.2 |     |          |         |     |
|       16 |       3 | 3.3  |     |       41 |       1 | 1.1 |     |          |         |     |
|       17 |       3 | 3.3  |     |       42 |       2 | 2.2 |     |          |         |     |
|       18 |       2 | 2.2  |     |       43 |       4 | 4.4 |     |          |         |     |
|       19 |       6 | 6.59 |     |       45 |       1 | 1.1 |     |          |         |     |
|       20 |       2 | 2.2  |     |       46 |       4 | 4.4 |     |          |         |     |
|       21 |       1 | 1.1  |     |       49 |       2 | 2.2 |     |          |         |     |
|       22 |       2 | 2.2  |     |       51 |       2 | 2.2 |     |          |         |     |
|       23 |       2 | 2.2  |     |       52 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 2.2  |     |       22 |       3 | 1.65 |     | 42       | 2       | 1.1  |
|        2 |       4 | 2.2  |     |       23 |       3 | 1.65 |     | 43       | 5       | 2.75 |
|        3 |       1 | 0.55 |     |       24 |       6 | 3.3  |     | 44       | 4       | 2.2  |
|        5 |       5 | 2.75 |     |       25 |       1 | 0.55 |     | 45       | 3       | 1.65 |
|        6 |       5 | 2.75 |     |       26 |       1 | 0.55 |     | 46       | 4       | 2.2  |
|        7 |       1 | 0.55 |     |       27 |       2 | 1.1  |     | 47       | 3       | 1.65 |
|        8 |       7 | 3.85 |     |       28 |       2 | 1.1  |     | 48       | 3       | 1.65 |
|        9 |       6 | 3.3  |     |       29 |       1 | 0.55 |     | 49       | 2       | 1.1  |
|       10 |       2 | 1.1  |     |       30 |       6 | 3.3  |     | 50       | 2       | 1.1  |
|       11 |       1 | 0.55 |     |       31 |       6 | 3.3  |     | 51       | 4       | 2.2  |
|       12 |       1 | 0.55 |     |       32 |       3 | 1.65 |     | 52       | 6       | 3.3  |
|       13 |       3 | 1.65 |     |       33 |       2 | 1.1  |     | 53       | 5       | 2.75 |
|       14 |       3 | 1.65 |     |       34 |       7 | 3.85 |     | 55       | 4       | 2.2  |
|       15 |       1 | 0.55 |     |       35 |       4 | 2.2  |     |          |         |      |
|       16 |       4 | 2.2  |     |       36 |       4 | 2.2  |     |          |         |      |
|       17 |       6 | 3.3  |     |       37 |       1 | 0.55 |     |          |         |      |
|       18 |       3 | 1.65 |     |       38 |       4 | 2.2  |     |          |         |      |
|       19 |       8 | 4.4  |     |       39 |       4 | 2.2  |     |          |         |      |
|       20 |       2 | 1.1  |     |       40 |       4 | 2.2  |     |          |         |      |
|       21 |       1 | 0.55 |     |       41 |       3 | 1.65 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.47 |     |       21 |       1 | 0.37 |     | 41       | 4       | 1.47 |
|        2 |       5 | 1.83 |     |       22 |       5 | 1.83 |     | 42       | 5       | 1.83 |
|        3 |       3 | 1.1  |     |       23 |       5 | 1.83 |     | 43       | 6       | 2.2  |
|        4 |       1 | 0.37 |     |       24 |       8 | 2.93 |     | 44       | 7       | 2.56 |
|        5 |       8 | 2.93 |     |       25 |       1 | 0.37 |     | 45       | 8       | 2.93 |
|        6 |       5 | 1.83 |     |       26 |       3 | 1.1  |     | 46       | 5       | 1.83 |
|        7 |       1 | 0.37 |     |       27 |       3 | 1.1  |     | 47       | 3       | 1.1  |
|        8 |       9 | 3.3  |     |       28 |       5 | 1.83 |     | 48       | 7       | 2.56 |
|        9 |       8 | 2.93 |     |       29 |       4 | 1.47 |     | 49       | 3       | 1.1  |
|       10 |       4 | 1.47 |     |       30 |       8 | 2.93 |     | 50       | 3       | 1.1  |
|       11 |       1 | 0.37 |     |       31 |      10 | 3.66 |     | 51       | 7       | 2.56 |
|       12 |       2 | 0.73 |     |       32 |       5 | 1.83 |     | 52       | 7       | 2.56 |
|       13 |       4 | 1.47 |     |       33 |       6 | 2.2  |     | 53       | 7       | 2.56 |
|       14 |       3 | 1.1  |     |       34 |      11 | 4.03 |     | 54       | 4       | 1.47 |
|       15 |       3 | 1.1  |     |       35 |       4 | 1.47 |     | 55       | 5       | 1.83 |
|       16 |       4 | 1.47 |     |       36 |       6 | 2.2  |     |          |         |      |
|       17 |       7 | 2.56 |     |       37 |       2 | 0.73 |     |          |         |      |
|       18 |       6 | 2.2  |     |       38 |       4 | 1.47 |     |          |         |      |
|       19 |       9 | 3.3  |     |       39 |       6 | 2.2  |     |          |         |      |
|       20 |       3 | 1.1  |     |       40 |       5 | 1.83 |     |          |         |      |



### ⚖️ [6/55] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 420        | 33.63     |
| 2:4                  | 312        | 24.98     |
| 4:2                  | 296        | 23.70     |
| 5:1                  | 117        | 9.37      |
| 1:5                  | 77         | 6.16      |
| 6:0                  | 20         | 1.60      |
| 0:6                  | 7          | 0.56      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 7          | 53.85     |
| 4:2                  | 2          | 15.38     |
| 2:4                  | 2          | 15.38     |
| 5:1                  | 2          | 15.38     |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 10         | 38.46     |
| 2:4                  | 8          | 30.77     |
| 4:2                  | 4          | 15.38     |
| 5:1                  | 3          | 11.54     |
| 1:5                  | 1          | 3.85      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 14         | 35.90     |
| 2:4                  | 11         | 28.21     |
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

No significant matches found in backtest period.



## 📈 Power 6/45 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                   |   page | process_time               |
|:-----------|------:|:-------------------------|-------:|:---------------------------|
| 2025-09-28 | 01412 | [8, 13, 18, 26, 36, 39]  |      0 | 2025-09-30T19:22:37.845940 |
| 2025-09-26 | 01411 | [12, 17, 19, 27, 28, 36] |      0 | 2025-09-30T19:22:37.846079 |
| 2025-09-24 | 01410 | [3, 5, 17, 31, 32, 40]   |      0 | 2025-09-30T19:22:37.846196 |
| 2025-09-21 | 01409 | [2, 3, 6, 21, 28, 38]    |      0 | 2025-09-30T19:22:37.846314 |
| 2025-09-19 | 01408 | [4, 6, 17, 18, 28, 41]   |      0 | 2025-09-19 21:19:53.906114 |
| 2025-09-17 | 01407 | [11, 23, 25, 35, 38, 45] |      0 | 2025-09-17 18:47:42.209975 |
| 2025-09-14 | 01406 | [3, 6, 9, 10, 30, 37]    |      0 | 2025-09-15 21:15:13.139917 |
| 2025-09-12 | 01405 | [17, 22, 24, 37, 42, 43] |      0 | 2025-09-12 21:43:38.569616 |
| 2025-09-10 | 01404 | [7, 10, 18, 20, 24, 36]  |      0 | 2025-09-12 21:43:38.569702 |
| 2025-09-07 | 01403 | [6, 29, 30, 39, 42, 44]  |      0 | 2025-09-12 21:43:38.569781 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     187 | 2.21 |     |       21 |     182 | 2.15 |     | 41       | 190     | 2.24 |
|        2 |     178 | 2.1  |     |       22 |     200 | 2.36 |     | 42       | 178     | 2.1  |
|        3 |     174 | 2.05 |     |       23 |     187 | 2.21 |     | 43       | 173     | 2.04 |
|        4 |     199 | 2.35 |     |       24 |     210 | 2.48 |     | 44       | 204     | 2.41 |
|        5 |     199 | 2.35 |     |       25 |     193 | 2.28 |     | 45       | 185     | 2.18 |
|        6 |     193 | 2.28 |     |       26 |     187 | 2.21 |     |          |         |      |
|        7 |     203 | 2.4  |     |       27 |     195 | 2.3  |     |          |         |      |
|        8 |     187 | 2.21 |     |       28 |     199 | 2.35 |     |          |         |      |
|        9 |     181 | 2.14 |     |       29 |     189 | 2.23 |     |          |         |      |
|       10 |     208 | 2.46 |     |       30 |     198 | 2.34 |     |          |         |      |
|       11 |     194 | 2.29 |     |       31 |     185 | 2.18 |     |          |         |      |
|       12 |     172 | 2.03 |     |       32 |     180 | 2.12 |     |          |         |      |
|       13 |     194 | 2.29 |     |       33 |     187 | 2.21 |     |          |         |      |
|       14 |     182 | 2.15 |     |       34 |     186 | 2.2  |     |          |         |      |
|       15 |     173 | 2.04 |     |       35 |     192 | 2.27 |     |          |         |      |
|       16 |     189 | 2.23 |     |       36 |     175 | 2.07 |     |          |         |      |
|       17 |     172 | 2.03 |     |       37 |     207 | 2.44 |     |          |         |      |
|       18 |     186 | 2.2  |     |       38 |     161 | 1.9  |     |          |         |      |
|       19 |     208 | 2.46 |     |       39 |     175 | 2.07 |     |          |         |      |
|       20 |     196 | 2.31 |     |       40 |     179 | 2.11 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 1.28 |     |       23 |       2 | 2.56 |     | 45       | 2       | 2.56 |
|        2 |       1 | 1.28 |     |       24 |       2 | 2.56 |     |          |         |      |
|        3 |       4 | 5.13 |     |       25 |       1 | 1.28 |     |          |         |      |
|        4 |       2 | 2.56 |     |       26 |       1 | 1.28 |     |          |         |      |
|        5 |       1 | 1.28 |     |       27 |       1 | 1.28 |     |          |         |      |
|        6 |       4 | 5.13 |     |       28 |       4 | 5.13 |     |          |         |      |
|        7 |       1 | 1.28 |     |       29 |       1 | 1.28 |     |          |         |      |
|        8 |       1 | 1.28 |     |       30 |       3 | 3.85 |     |          |         |      |
|        9 |       1 | 1.28 |     |       31 |       1 | 1.28 |     |          |         |      |
|       10 |       3 | 3.85 |     |       32 |       2 | 2.56 |     |          |         |      |
|       11 |       1 | 1.28 |     |       35 |       1 | 1.28 |     |          |         |      |
|       12 |       1 | 1.28 |     |       36 |       3 | 3.85 |     |          |         |      |
|       13 |       1 | 1.28 |     |       37 |       2 | 2.56 |     |          |         |      |
|       14 |       2 | 2.56 |     |       38 |       3 | 3.85 |     |          |         |      |
|       17 |       4 | 5.13 |     |       39 |       2 | 2.56 |     |          |         |      |
|       18 |       3 | 3.85 |     |       40 |       1 | 1.28 |     |          |         |      |
|       19 |       1 | 1.28 |     |       41 |       2 | 2.56 |     |          |         |      |
|       20 |       2 | 2.56 |     |       42 |       2 | 2.56 |     |          |         |      |
|       21 |       2 | 2.56 |     |       43 |       2 | 2.56 |     |          |         |      |
|       22 |       2 | 2.56 |     |       44 |       2 | 2.56 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.28 |     |       22 |       3 | 1.92 |     | 43       | 5       | 3.21 |
|        2 |       3 | 1.92 |     |       23 |       2 | 1.28 |     | 44       | 2       | 1.28 |
|        3 |       6 | 3.85 |     |       24 |       5 | 3.21 |     | 45       | 4       | 2.56 |
|        4 |       4 | 2.56 |     |       25 |       1 | 0.64 |     |          |         |      |
|        5 |       4 | 2.56 |     |       26 |       5 | 3.21 |     |          |         |      |
|        6 |       4 | 2.56 |     |       27 |       4 | 2.56 |     |          |         |      |
|        7 |       1 | 0.64 |     |       28 |       7 | 4.49 |     |          |         |      |
|        8 |       1 | 0.64 |     |       29 |       4 | 2.56 |     |          |         |      |
|        9 |       4 | 2.56 |     |       30 |       5 | 3.21 |     |          |         |      |
|       10 |       6 | 3.85 |     |       31 |       4 | 2.56 |     |          |         |      |
|       11 |       3 | 1.92 |     |       32 |       4 | 2.56 |     |          |         |      |
|       12 |       2 | 1.28 |     |       34 |       1 | 0.64 |     |          |         |      |
|       13 |       3 | 1.92 |     |       35 |       4 | 2.56 |     |          |         |      |
|       14 |       4 | 2.56 |     |       36 |       6 | 3.85 |     |          |         |      |
|       15 |       2 | 1.28 |     |       37 |       4 | 2.56 |     |          |         |      |
|       17 |       5 | 3.21 |     |       38 |       6 | 3.85 |     |          |         |      |
|       18 |       5 | 3.21 |     |       39 |       4 | 2.56 |     |          |         |      |
|       19 |       1 | 0.64 |     |       40 |       2 | 1.28 |     |          |         |      |
|       20 |       4 | 2.56 |     |       41 |       2 | 1.28 |     |          |         |      |
|       21 |       3 | 1.92 |     |       42 |       5 | 3.21 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.28 |     |       21 |       6 | 2.56 |     | 41       | 4       | 1.71 |
|        2 |       4 | 1.71 |     |       22 |       6 | 2.56 |     | 42       | 8       | 3.42 |
|        3 |       7 | 2.99 |     |       23 |       3 | 1.28 |     | 43       | 6       | 2.56 |
|        4 |       4 | 1.71 |     |       24 |       8 | 3.42 |     | 44       | 4       | 1.71 |
|        5 |       5 | 2.14 |     |       25 |       1 | 0.43 |     | 45       | 9       | 3.85 |
|        6 |       6 | 2.56 |     |       26 |       7 | 2.99 |     |          |         |      |
|        7 |       4 | 1.71 |     |       27 |       6 | 2.56 |     |          |         |      |
|        8 |       3 | 1.28 |     |       28 |       9 | 3.85 |     |          |         |      |
|        9 |       7 | 2.99 |     |       29 |       6 | 2.56 |     |          |         |      |
|       10 |       6 | 2.56 |     |       30 |       7 | 2.99 |     |          |         |      |
|       11 |       6 | 2.56 |     |       31 |       4 | 1.71 |     |          |         |      |
|       12 |       4 | 1.71 |     |       32 |       6 | 2.56 |     |          |         |      |
|       13 |       5 | 2.14 |     |       33 |       1 | 0.43 |     |          |         |      |
|       14 |       6 | 2.56 |     |       34 |       4 | 1.71 |     |          |         |      |
|       15 |       2 | 0.85 |     |       35 |       6 | 2.56 |     |          |         |      |
|       16 |       2 | 0.85 |     |       36 |       8 | 3.42 |     |          |         |      |
|       17 |       6 | 2.56 |     |       37 |       6 | 2.56 |     |          |         |      |
|       18 |       5 | 2.14 |     |       38 |       7 | 2.99 |     |          |         |      |
|       19 |       2 | 0.85 |     |       39 |       6 | 2.56 |     |          |         |      |
|       20 |       7 | 2.99 |     |       40 |       2 | 0.85 |     |          |         |      |



### ⚖️ [6/45] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 494        | 34.99     |
| 4:2                  | 336        | 23.80     |
| 2:4                  | 310        | 21.95     |
| 5:1                  | 129        | 9.14      |
| 1:5                  | 108        | 7.65      |
| 6:0                  | 21         | 1.49      |
| 0:6                  | 14         | 0.99      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 5          | 38.46     |
| 2:4                  | 4          | 30.77     |
| 1:5                  | 2          | 15.38     |
| 4:2                  | 1          | 7.69      |
| 5:1                  | 1          | 7.69      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 11         | 42.31     |
| 2:4                  | 7          | 26.92     |
| 4:2                  | 3          | 11.54     |
| 1:5                  | 3          | 11.54     |
| 5:1                  | 2          | 7.69      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 14         | 35.90     |
| 2:4                  | 12         | 30.77     |
| 4:2                  | 5          | 12.82     |
| 1:5                  | 4          | 10.26     |
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

