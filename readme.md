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
| Power 655 |          1252 | 2017-08-01   | 2025-10-07 |            1252 | 00001      | 01252       |
| Power 645 |          1416 | 2016-07-20   | 2025-10-08 |            1416 | 00001      | 01416       |
| Power 535 |            96 | 2025-06-29   | 2025-10-08 |             190 | 00001      | 00204       |
| Keno      |           343 | 2022-12-04   | 2025-09-30 |           44920 | #0110271   | #0254111    |
| 3D        |           987 | 2019-04-22   | 2025-10-08 |             987 | 00001      | 00987       |
| 3D Pro    |           633 | 2021-09-14   | 2025-10-07 |             633 | 00001      | 00633       |
| Bingo18   |           293 | 2024-12-03   | 2025-09-30 |           46246 | 0083123    | 0130917     |

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
| 2025-10-07 | 01252 | [19, 22, 35, 37, 43, 45, 29] |      0 | 2025-10-08 21:40:23.214427 |
| 2025-10-04 | 01251 | [22, 33, 35, 36, 38, 40, 7]  |      0 | 2025-10-05 17:04:48.001158 |
| 2025-10-02 | 01250 | [1, 2, 20, 24, 27, 42, 43]   |      0 | 2025-10-05 17:04:48.001330 |
| 2025-09-30 | 01249 | [17, 23, 34, 39, 46, 52, 8]  |      0 | 2025-09-30 19:22:07.239312 |
| 2025-09-27 | 01248 | [8, 13, 19, 24, 39, 46, 1]   |      0 | 2025-09-30 19:22:07.239405 |
| 2025-09-25 | 01247 | [5, 17, 30, 31, 38, 53, 8]   |      0 | 2025-09-30 19:22:07.239490 |
| 2025-09-23 | 01246 | [8, 18, 19, 34, 41, 46, 38]  |      0 | 2025-09-30 19:22:07.239573 |
| 2025-09-20 | 01245 | [8, 13, 14, 19, 36, 43, 30]  |      0 | 2025-09-21 07:37:04.165282 |
| 2025-09-18 | 01244 | [2, 3, 8, 27, 38, 55, 20]    |      0 | 2025-09-18 19:49:45.191045 |
| 2025-09-16 | 01243 | [17, 19, 28, 39, 43, 53, 33] |      0 | 2025-09-16 19:20:04.498817 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     172 | 1.96 |     |       21 |     152 | 1.73 |     | 41       | 187     | 2.13 |
|        2 |     147 | 1.68 |     |       22 |     180 | 2.05 |     | 42       | 163     | 1.86 |
|        3 |     170 | 1.94 |     |       23 |     172 | 1.96 |     | 43       | 180     | 2.05 |
|        4 |     132 | 1.51 |     |       24 |     163 | 1.86 |     | 44       | 167     | 1.91 |
|        5 |     160 | 1.83 |     |       25 |     141 | 1.61 |     | 45       | 160     | 1.83 |
|        6 |     136 | 1.55 |     |       26 |     145 | 1.65 |     | 46       | 164     | 1.87 |
|        7 |     136 | 1.55 |     |       27 |     146 | 1.67 |     | 47       | 161     | 1.84 |
|        8 |     171 | 1.95 |     |       28 |     140 | 1.6  |     | 48       | 170     | 1.94 |
|        9 |     176 | 2.01 |     |       29 |     167 | 1.91 |     | 49       | 161     | 1.84 |
|       10 |     148 | 1.69 |     |       30 |     142 | 1.62 |     | 50       | 159     | 1.81 |
|       11 |     163 | 1.86 |     |       31 |     167 | 1.91 |     | 51       | 183     | 2.09 |
|       12 |     165 | 1.88 |     |       32 |     164 | 1.87 |     | 52       | 165     | 1.88 |
|       13 |     152 | 1.73 |     |       33 |     160 | 1.83 |     | 53       | 169     | 1.93 |
|       14 |     158 | 1.8  |     |       34 |     181 | 2.07 |     | 54       | 149     | 1.7  |
|       15 |     149 | 1.7  |     |       35 |     157 | 1.79 |     | 55       | 157     | 1.79 |
|       16 |     148 | 1.69 |     |       36 |     149 | 1.7  |     |          |         |      |
|       17 |     148 | 1.69 |     |       37 |     144 | 1.64 |     |          |         |      |
|       18 |     163 | 1.86 |     |       38 |     149 | 1.7  |     |          |         |      |
|       19 |     162 | 1.85 |     |       39 |     152 | 1.73 |     |          |         |      |
|       20 |     168 | 1.92 |     |       40 |     173 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       2 | 2.2  |     |       28 |       1 | 1.1 |     | 53       | 2       | 2.2 |
|        2 |       4 | 4.4  |     |       29 |       1 | 1.1 |     | 55       | 2       | 2.2 |
|        3 |       1 | 1.1  |     |       30 |       2 | 2.2 |     |          |         |     |
|        5 |       1 | 1.1  |     |       31 |       2 | 2.2 |     |          |         |     |
|        6 |       1 | 1.1  |     |       33 |       2 | 2.2 |     |          |         |     |
|        7 |       2 | 2.2  |     |       34 |       2 | 2.2 |     |          |         |     |
|        8 |       6 | 6.59 |     |       35 |       2 | 2.2 |     |          |         |     |
|       13 |       2 | 2.2  |     |       36 |       2 | 2.2 |     |          |         |     |
|       14 |       1 | 1.1  |     |       37 |       1 | 1.1 |     |          |         |     |
|       15 |       1 | 1.1  |     |       38 |       4 | 4.4 |     |          |         |     |
|       16 |       2 | 2.2  |     |       39 |       3 | 3.3 |     |          |         |     |
|       17 |       3 | 3.3  |     |       40 |       2 | 2.2 |     |          |         |     |
|       18 |       2 | 2.2  |     |       41 |       1 | 1.1 |     |          |         |     |
|       19 |       5 | 5.49 |     |       42 |       2 | 2.2 |     |          |         |     |
|       20 |       3 | 3.3  |     |       43 |       4 | 4.4 |     |          |         |     |
|       21 |       1 | 1.1  |     |       45 |       2 | 2.2 |     |          |         |     |
|       22 |       2 | 2.2  |     |       46 |       4 | 4.4 |     |          |         |     |
|       23 |       1 | 1.1  |     |       49 |       1 | 1.1 |     |          |         |     |
|       24 |       3 | 3.3  |     |       51 |       1 | 1.1 |     |          |         |     |
|       27 |       3 | 3.3  |     |       52 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 2.75 |     |       23 |       3 | 1.65 |     | 43       | 7       | 3.85 |
|        2 |       5 | 2.75 |     |       24 |       5 | 2.75 |     | 44       | 4       | 2.2  |
|        3 |       1 | 0.55 |     |       25 |       1 | 0.55 |     | 45       | 3       | 1.65 |
|        5 |       5 | 2.75 |     |       26 |       1 | 0.55 |     | 46       | 4       | 2.2  |
|        6 |       4 | 2.2  |     |       27 |       3 | 1.65 |     | 47       | 2       | 1.1  |
|        7 |       2 | 1.1  |     |       28 |       2 | 1.1  |     | 48       | 2       | 1.1  |
|        8 |       6 | 3.3  |     |       29 |       1 | 0.55 |     | 49       | 2       | 1.1  |
|        9 |       6 | 3.3  |     |       30 |       6 | 3.3  |     | 50       | 2       | 1.1  |
|       10 |       2 | 1.1  |     |       31 |       4 | 2.2  |     | 51       | 3       | 1.65 |
|       11 |       1 | 0.55 |     |       32 |       2 | 1.1  |     | 52       | 4       | 2.2  |
|       13 |       3 | 1.65 |     |       33 |       2 | 1.1  |     | 53       | 4       | 2.2  |
|       14 |       3 | 1.65 |     |       34 |       6 | 3.3  |     | 55       | 4       | 2.2  |
|       15 |       1 | 0.55 |     |       35 |       5 | 2.75 |     |          |         |      |
|       16 |       4 | 2.2  |     |       36 |       5 | 2.75 |     |          |         |      |
|       17 |       6 | 3.3  |     |       37 |       2 | 1.1  |     |          |         |      |
|       18 |       3 | 1.65 |     |       38 |       5 | 2.75 |     |          |         |      |
|       19 |       9 | 4.95 |     |       39 |       3 | 1.65 |     |          |         |      |
|       20 |       3 | 1.65 |     |       40 |       5 | 2.75 |     |          |         |      |
|       21 |       1 | 0.55 |     |       41 |       2 | 1.1  |     |          |         |      |
|       22 |       5 | 2.75 |     |       42 |       3 | 1.65 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 1.83 |     |       21 |       1 | 0.37 |     | 41       | 4       | 1.47 |
|        2 |       6 | 2.2  |     |       22 |       6 | 2.2  |     | 42       | 5       | 1.83 |
|        3 |       2 | 0.73 |     |       23 |       4 | 1.47 |     | 43       | 8       | 2.93 |
|        4 |       1 | 0.37 |     |       24 |       8 | 2.93 |     | 44       | 7       | 2.56 |
|        5 |       8 | 2.93 |     |       25 |       1 | 0.37 |     | 45       | 7       | 2.56 |
|        6 |       5 | 1.83 |     |       26 |       3 | 1.1  |     | 46       | 5       | 1.83 |
|        7 |       2 | 0.73 |     |       27 |       3 | 1.1  |     | 47       | 3       | 1.1  |
|        8 |       9 | 3.3  |     |       28 |       5 | 1.83 |     | 48       | 6       | 2.2  |
|        9 |       8 | 2.93 |     |       29 |       4 | 1.47 |     | 49       | 3       | 1.1  |
|       10 |       4 | 1.47 |     |       30 |       8 | 2.93 |     | 50       | 2       | 0.73 |
|       11 |       1 | 0.37 |     |       31 |       8 | 2.93 |     | 51       | 6       | 2.2  |
|       12 |       2 | 0.73 |     |       32 |       4 | 1.47 |     | 52       | 7       | 2.56 |
|       13 |       4 | 1.47 |     |       33 |       7 | 2.56 |     | 53       | 7       | 2.56 |
|       14 |       3 | 1.1  |     |       34 |      11 | 4.03 |     | 54       | 2       | 0.73 |
|       15 |       2 | 0.73 |     |       35 |       6 | 2.2  |     | 55       | 4       | 1.47 |
|       16 |       4 | 1.47 |     |       36 |       7 | 2.56 |     |          |         |      |
|       17 |       7 | 2.56 |     |       37 |       3 | 1.1  |     |          |         |      |
|       18 |       5 | 1.83 |     |       38 |       5 | 1.83 |     |          |         |      |
|       19 |       9 | 3.3  |     |       39 |       6 | 2.2  |     |          |         |      |
|       20 |       4 | 1.47 |     |       40 |       6 | 2.2  |     |          |         |      |



### ⚖️ [6/55] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 420        | 33.55     |
| 2:4                  | 314        | 25.08     |
| 4:2                  | 296        | 23.64     |
| 5:1                  | 118        | 9.42      |
| 1:5                  | 77         | 6.15      |
| 6:0                  | 20         | 1.60      |
| 0:6                  | 7          | 0.56      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 6          | 46.15     |
| 2:4                  | 4          | 30.77     |
| 5:1                  | 2          | 15.38     |
| 4:2                  | 1          | 7.69      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 9          | 34.62     |
| 3:3                  | 9          | 34.62     |
| 5:1                  | 4          | 15.38     |
| 4:2                  | 3          | 11.54     |
| 1:5                  | 1          | 3.85      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 14         | 35.90     |
| 2:4                  | 13         | 33.33     |
| 4:2                  | 6          | 15.38     |
| 5:1                  | 4          | 10.26     |
| 1:5                  | 2          | 5.13      |


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
| 2025-10-08 | 01416 | [8, 10, 11, 18, 23, 32]  |      0 | 2025-10-08T21:40:27.958251 |
| 2025-10-05 | 01415 | [5, 14, 22, 28, 32, 39]  |      0 | 2025-10-08T21:40:27.958348 |
| 2025-10-03 | 01414 | [29, 31, 32, 33, 34, 35] |      0 | 2025-10-05 17:05:12.128384 |
| 2025-10-01 | 01413 | [3, 6, 7, 19, 30, 35]    |      0 | 2025-10-05 17:05:12.128562 |
| 2025-09-28 | 01412 | [8, 13, 18, 26, 36, 39]  |      0 | 2025-09-30 19:22:37.845940 |
| 2025-09-26 | 01411 | [12, 17, 19, 27, 28, 36] |      0 | 2025-09-30 19:22:37.846079 |
| 2025-09-24 | 01410 | [3, 5, 17, 31, 32, 40]   |      0 | 2025-09-30 19:22:37.846196 |
| 2025-09-21 | 01409 | [2, 3, 6, 21, 28, 38]    |      0 | 2025-09-30 19:22:37.846314 |
| 2025-09-19 | 01408 | [4, 6, 17, 18, 28, 41]   |      0 | 2025-09-19 21:19:53.906114 |
| 2025-09-17 | 01407 | [11, 23, 25, 35, 38, 45] |      0 | 2025-09-17 18:47:42.209975 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     187 | 2.2  |     |       21 |     182 | 2.14 |     | 41       | 190     | 2.24 |
|        2 |     178 | 2.1  |     |       22 |     201 | 2.37 |     | 42       | 178     | 2.1  |
|        3 |     175 | 2.06 |     |       23 |     188 | 2.21 |     | 43       | 173     | 2.04 |
|        4 |     199 | 2.34 |     |       24 |     210 | 2.47 |     | 44       | 204     | 2.4  |
|        5 |     200 | 2.35 |     |       25 |     193 | 2.27 |     | 45       | 185     | 2.18 |
|        6 |     194 | 2.28 |     |       26 |     187 | 2.2  |     |          |         |      |
|        7 |     204 | 2.4  |     |       27 |     195 | 2.3  |     |          |         |      |
|        8 |     188 | 2.21 |     |       28 |     200 | 2.35 |     |          |         |      |
|        9 |     181 | 2.13 |     |       29 |     190 | 2.24 |     |          |         |      |
|       10 |     209 | 2.46 |     |       30 |     199 | 2.34 |     |          |         |      |
|       11 |     195 | 2.3  |     |       31 |     186 | 2.19 |     |          |         |      |
|       12 |     172 | 2.02 |     |       32 |     183 | 2.15 |     |          |         |      |
|       13 |     194 | 2.28 |     |       33 |     188 | 2.21 |     |          |         |      |
|       14 |     183 | 2.15 |     |       34 |     187 | 2.2  |     |          |         |      |
|       15 |     173 | 2.04 |     |       35 |     194 | 2.28 |     |          |         |      |
|       16 |     189 | 2.22 |     |       36 |     175 | 2.06 |     |          |         |      |
|       17 |     172 | 2.02 |     |       37 |     207 | 2.44 |     |          |         |      |
|       18 |     187 | 2.2  |     |       38 |     161 | 1.9  |     |          |         |      |
|       19 |     209 | 2.46 |     |       39 |     176 | 2.07 |     |          |         |      |
|       20 |     196 | 2.31 |     |       40 |     179 | 2.11 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        2 |       1 | 1.28 |     |       24 |       2 | 2.56 |     | 45       | 1       | 1.28 |
|        3 |       4 | 5.13 |     |       25 |       1 | 1.28 |     |          |         |      |
|        4 |       1 | 1.28 |     |       26 |       1 | 1.28 |     |          |         |      |
|        5 |       2 | 2.56 |     |       27 |       1 | 1.28 |     |          |         |      |
|        6 |       4 | 5.13 |     |       28 |       4 | 5.13 |     |          |         |      |
|        7 |       2 | 2.56 |     |       29 |       1 | 1.28 |     |          |         |      |
|        8 |       2 | 2.56 |     |       30 |       2 | 2.56 |     |          |         |      |
|        9 |       1 | 1.28 |     |       31 |       2 | 2.56 |     |          |         |      |
|       10 |       3 | 3.85 |     |       32 |       4 | 5.13 |     |          |         |      |
|       11 |       2 | 2.56 |     |       33 |       1 | 1.28 |     |          |         |      |
|       12 |       1 | 1.28 |     |       34 |       1 | 1.28 |     |          |         |      |
|       13 |       1 | 1.28 |     |       35 |       3 | 3.85 |     |          |         |      |
|       14 |       1 | 1.28 |     |       36 |       3 | 3.85 |     |          |         |      |
|       17 |       4 | 5.13 |     |       37 |       2 | 2.56 |     |          |         |      |
|       18 |       4 | 5.13 |     |       38 |       2 | 2.56 |     |          |         |      |
|       19 |       2 | 2.56 |     |       39 |       2 | 2.56 |     |          |         |      |
|       20 |       1 | 1.28 |     |       40 |       1 | 1.28 |     |          |         |      |
|       21 |       1 | 1.28 |     |       41 |       1 | 1.28 |     |          |         |      |
|       22 |       2 | 2.56 |     |       42 |       1 | 1.28 |     |          |         |      |
|       23 |       2 | 2.56 |     |       43 |       1 | 1.28 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.28 |     |       22 |       4 | 2.56 |     | 42       | 5       | 3.21 |
|        2 |       3 | 1.92 |     |       23 |       3 | 1.92 |     | 43       | 4       | 2.56 |
|        3 |       6 | 3.85 |     |       24 |       4 | 2.56 |     | 44       | 2       | 1.28 |
|        4 |       4 | 2.56 |     |       25 |       1 | 0.64 |     | 45       | 4       | 2.56 |
|        5 |       3 | 1.92 |     |       26 |       3 | 1.92 |     |          |         |      |
|        6 |       5 | 3.21 |     |       27 |       3 | 1.92 |     |          |         |      |
|        7 |       2 | 1.28 |     |       28 |       8 | 5.13 |     |          |         |      |
|        8 |       2 | 1.28 |     |       29 |       3 | 1.92 |     |          |         |      |
|        9 |       4 | 2.56 |     |       30 |       5 | 3.21 |     |          |         |      |
|       10 |       7 | 4.49 |     |       31 |       4 | 2.56 |     |          |         |      |
|       11 |       3 | 1.92 |     |       32 |       7 | 4.49 |     |          |         |      |
|       12 |       1 | 0.64 |     |       33 |       1 | 0.64 |     |          |         |      |
|       13 |       3 | 1.92 |     |       34 |       1 | 0.64 |     |          |         |      |
|       14 |       3 | 1.92 |     |       35 |       6 | 3.85 |     |          |         |      |
|       15 |       2 | 1.28 |     |       36 |       5 | 3.21 |     |          |         |      |
|       17 |       4 | 2.56 |     |       37 |       3 | 1.92 |     |          |         |      |
|       18 |       5 | 3.21 |     |       38 |       4 | 2.56 |     |          |         |      |
|       19 |       2 | 1.28 |     |       39 |       5 | 3.21 |     |          |         |      |
|       20 |       3 | 1.92 |     |       40 |       2 | 1.28 |     |          |         |      |
|       21 |       3 | 1.92 |     |       41 |       2 | 1.28 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.28 |     |       21 |       4 | 1.71 |     | 41       | 2       | 0.85 |
|        2 |       4 | 1.71 |     |       22 |       7 | 2.99 |     | 42       | 8       | 3.42 |
|        3 |       8 | 3.42 |     |       23 |       3 | 1.28 |     | 43       | 6       | 2.56 |
|        4 |       4 | 1.71 |     |       24 |       8 | 3.42 |     | 44       | 3       | 1.28 |
|        5 |       5 | 2.14 |     |       25 |       1 | 0.43 |     | 45       | 7       | 2.99 |
|        6 |       7 | 2.99 |     |       26 |       7 | 2.99 |     |          |         |      |
|        7 |       3 | 1.28 |     |       27 |       6 | 2.56 |     |          |         |      |
|        8 |       2 | 0.85 |     |       28 |       9 | 3.85 |     |          |         |      |
|        9 |       6 | 2.56 |     |       29 |       6 | 2.56 |     |          |         |      |
|       10 |       7 | 2.99 |     |       30 |       7 | 2.99 |     |          |         |      |
|       11 |       7 | 2.99 |     |       31 |       5 | 2.14 |     |          |         |      |
|       12 |       3 | 1.28 |     |       32 |       8 | 3.42 |     |          |         |      |
|       13 |       4 | 1.71 |     |       33 |       1 | 0.43 |     |          |         |      |
|       14 |       7 | 2.99 |     |       34 |       4 | 1.71 |     |          |         |      |
|       15 |       2 | 0.85 |     |       35 |       8 | 3.42 |     |          |         |      |
|       16 |       1 | 0.43 |     |       36 |       7 | 2.99 |     |          |         |      |
|       17 |       6 | 2.56 |     |       37 |       6 | 2.56 |     |          |         |      |
|       18 |       6 | 2.56 |     |       38 |       7 | 2.99 |     |          |         |      |
|       19 |       3 | 1.28 |     |       39 |       7 | 2.99 |     |          |         |      |
|       20 |       7 | 2.99 |     |       40 |       2 | 0.85 |     |          |         |      |



### ⚖️ [6/45] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 494        | 34.89     |
| 4:2                  | 338        | 23.87     |
| 2:4                  | 312        | 22.03     |
| 5:1                  | 129        | 9.11      |
| 1:5                  | 108        | 7.63      |
| 6:0                  | 21         | 1.48      |
| 0:6                  | 14         | 0.99      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 5          | 38.46     |
| 4:2                  | 3          | 23.08     |
| 3:3                  | 3          | 23.08     |
| 5:1                  | 1          | 7.69      |
| 1:5                  | 1          | 7.69      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 8          | 30.77     |
| 3:3                  | 8          | 30.77     |
| 4:2                  | 5          | 19.23     |
| 1:5                  | 3          | 11.54     |
| 5:1                  | 2          | 7.69      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 14         | 35.90     |
| 2:4                  | 12         | 30.77     |
| 4:2                  | 6          | 15.38     |
| 1:5                  | 4          | 10.26     |
| 5:1                  | 3          | 7.69      |


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

