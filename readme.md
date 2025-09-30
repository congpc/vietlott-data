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
| Power 655 |          1245 | 2017-08-01   | 2025-09-20 |            1245 | 00001      | 01245       |
| Power 645 |          1408 | 2016-07-20   | 2025-09-19 |            1408 | 00001      | 01408       |
| Power 535 |            87 | 2025-06-29   | 2025-09-29 |             172 | 00001      | 00186       |
| Keno      |           343 | 2022-12-04   | 2025-09-30 |           44920 | #0110271   | #0254111    |
| 3D        |           983 | 2019-04-22   | 2025-09-29 |             983 | 00001      | 00983       |
| 3D Pro    |           629 | 2021-09-14   | 2025-09-27 |             629 | 00001      | 00629       |
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
| 2025-08-07 | [6, 24, 31, 32, 39, 48, 52] | [31, 24, 48, 52, 6, 25] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-09-20 | 01245 | [8, 13, 14, 19, 36, 43, 30]  |      0 | 2025-09-21T07:37:04.165282 |
| 2025-09-18 | 01244 | [2, 3, 8, 27, 38, 55, 20]    |      0 | 2025-09-18 19:49:45.191045 |
| 2025-09-16 | 01243 | [17, 19, 28, 39, 43, 53, 33] |      0 | 2025-09-16 19:20:04.498817 |
| 2025-09-13 | 01242 | [2, 7, 15, 18, 24, 27, 45]   |      0 | 2025-09-13 18:44:39.730760 |
| 2025-09-11 | 01241 | [6, 16, 46, 49, 51, 55, 42]  |      0 | 2025-09-12 21:43:12.873808 |
| 2025-09-09 | 01240 | [16, 20, 21, 31, 40, 52, 2]  |      0 | 2025-09-12 21:43:12.873917 |
| 2025-09-06 | 01239 | [9, 11, 19, 22, 34, 43, 31]  |      0 | 2025-09-12 21:43:12.874010 |
| 2025-09-04 | 01238 | [9, 19, 23, 42, 49, 53, 40]  |      0 | 2025-09-12 21:43:12.874103 |
| 2025-09-02 | 01237 | [9, 16, 22, 25, 30, 51, 43]  |      0 | 2025-09-03 09:49:14.784413 |
| 2025-08-30 | 01236 | [2, 17, 19, 24, 30, 44, 34]  |      0 | 2025-08-31 12:07:10.223130 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     170 | 1.95 |     |       21 |     152 | 1.74 |     | 41       | 186     | 2.13 |
|        2 |     146 | 1.68 |     |       22 |     178 | 2.04 |     | 42       | 162     | 1.86 |
|        3 |     170 | 1.95 |     |       23 |     171 | 1.96 |     | 43       | 178     | 2.04 |
|        4 |     132 | 1.51 |     |       24 |     161 | 1.85 |     | 44       | 167     | 1.92 |
|        5 |     159 | 1.82 |     |       25 |     141 | 1.62 |     | 45       | 159     | 1.82 |
|        6 |     136 | 1.56 |     |       26 |     145 | 1.66 |     | 46       | 161     | 1.85 |
|        7 |     135 | 1.55 |     |       27 |     145 | 1.66 |     | 47       | 161     | 1.85 |
|        8 |     167 | 1.92 |     |       28 |     140 | 1.61 |     | 48       | 170     | 1.95 |
|        9 |     176 | 2.02 |     |       29 |     166 | 1.9  |     | 49       | 161     | 1.85 |
|       10 |     148 | 1.7  |     |       30 |     141 | 1.62 |     | 50       | 159     | 1.82 |
|       11 |     163 | 1.87 |     |       31 |     166 | 1.9  |     | 51       | 183     | 2.1  |
|       12 |     165 | 1.89 |     |       32 |     164 | 1.88 |     | 52       | 164     | 1.88 |
|       13 |     151 | 1.73 |     |       33 |     159 | 1.82 |     | 53       | 168     | 1.93 |
|       14 |     158 | 1.81 |     |       34 |     179 | 2.05 |     | 54       | 149     | 1.71 |
|       15 |     149 | 1.71 |     |       35 |     155 | 1.78 |     | 55       | 157     | 1.8  |
|       16 |     148 | 1.7  |     |       36 |     148 | 1.7  |     |          |         |      |
|       17 |     146 | 1.68 |     |       37 |     143 | 1.64 |     |          |         |      |
|       18 |     162 | 1.86 |     |       38 |     146 | 1.68 |     |          |         |      |
|       19 |     159 | 1.82 |     |       39 |     150 | 1.72 |     |          |         |      |
|       20 |     167 | 1.92 |     |       40 |     172 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        2 |       3 | 4.76 |     | 27       | 2       | 3.17 |
|        3 |       1 | 1.59 |     | 28       | 1       | 1.59 |
|        6 |       1 | 1.59 |     | 30       | 2       | 3.17 |
|        7 |       1 | 1.59 |     | 31       | 2       | 3.17 |
|        8 |       2 | 3.17 |     | 33       | 1       | 1.59 |
|        9 |       3 | 4.76 |     | 34       | 1       | 1.59 |
|       11 |       1 | 1.59 |     | 36       | 1       | 1.59 |
|       13 |       1 | 1.59 |     | 38       | 1       | 1.59 |
|       14 |       1 | 1.59 |     | 39       | 1       | 1.59 |
|       15 |       1 | 1.59 |     | 40       | 2       | 3.17 |
|       16 |       3 | 4.76 |     | 42       | 2       | 3.17 |
|       17 |       1 | 1.59 |     | 43       | 4       | 6.35 |
|       18 |       1 | 1.59 |     | 45       | 1       | 1.59 |
|       19 |       4 | 6.35 |     | 46       | 1       | 1.59 |
|       20 |       2 | 3.17 |     | 49       | 2       | 3.17 |
|       21 |       1 | 1.59 |     | 51       | 2       | 3.17 |
|       22 |       2 | 3.17 |     | 52       | 1       | 1.59 |
|       23 |       1 | 1.59 |     | 53       | 2       | 3.17 |
|       24 |       1 | 1.59 |     | 55       | 2       | 3.17 |
|       25 |       1 | 1.59 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.95 |     |       22 |       3 | 1.95 |     | 42       | 2       | 1.3  |
|        2 |       4 | 2.6  |     |       23 |       2 | 1.3  |     | 43       | 5       | 3.25 |
|        3 |       1 | 0.65 |     |       24 |       5 | 3.25 |     | 44       | 4       | 2.6  |
|        5 |       4 | 2.6  |     |       25 |       1 | 0.65 |     | 45       | 3       | 1.95 |
|        6 |       5 | 3.25 |     |       26 |       1 | 0.65 |     | 46       | 1       | 0.65 |
|        7 |       1 | 0.65 |     |       27 |       2 | 1.3  |     | 47       | 3       | 1.95 |
|        8 |       3 | 1.95 |     |       28 |       2 | 1.3  |     | 48       | 3       | 1.95 |
|        9 |       6 | 3.9  |     |       29 |       1 | 0.65 |     | 49       | 2       | 1.3  |
|       10 |       2 | 1.3  |     |       30 |       5 | 3.25 |     | 50       | 2       | 1.3  |
|       11 |       1 | 0.65 |     |       31 |       5 | 3.25 |     | 51       | 4       | 2.6  |
|       12 |       1 | 0.65 |     |       32 |       3 | 1.95 |     | 52       | 5       | 3.25 |
|       13 |       2 | 1.3  |     |       33 |       2 | 1.3  |     | 53       | 4       | 2.6  |
|       14 |       3 | 1.95 |     |       34 |       5 | 3.25 |     | 55       | 4       | 2.6  |
|       15 |       1 | 0.65 |     |       35 |       4 | 2.6  |     |          |         |      |
|       16 |       4 | 2.6  |     |       36 |       4 | 2.6  |     |          |         |      |
|       17 |       4 | 2.6  |     |       37 |       1 | 0.65 |     |          |         |      |
|       18 |       2 | 1.3  |     |       38 |       2 | 1.3  |     |          |         |      |
|       19 |       6 | 3.9  |     |       39 |       2 | 1.3  |     |          |         |      |
|       20 |       2 | 1.3  |     |       40 |       4 | 2.6  |     |          |         |      |
|       21 |       1 | 0.65 |     |       41 |       2 | 1.3  |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.22 |     |       21 |       1 | 0.41 |     | 41       | 3       | 1.22 |
|        2 |       5 | 2.04 |     |       22 |       5 | 2.04 |     | 42       | 5       | 2.04 |
|        3 |       3 | 1.22 |     |       23 |       4 | 1.63 |     | 43       | 6       | 2.45 |
|        4 |       1 | 0.41 |     |       24 |       7 | 2.86 |     | 44       | 7       | 2.86 |
|        5 |       7 | 2.86 |     |       25 |       1 | 0.41 |     | 45       | 8       | 3.27 |
|        6 |       5 | 2.04 |     |       26 |       3 | 1.22 |     | 46       | 2       | 0.82 |
|        7 |       1 | 0.41 |     |       27 |       3 | 1.22 |     | 47       | 3       | 1.22 |
|        8 |       5 | 2.04 |     |       28 |       5 | 2.04 |     | 48       | 7       | 2.86 |
|        9 |       8 | 3.27 |     |       29 |       4 | 1.63 |     | 49       | 3       | 1.22 |
|       10 |       4 | 1.63 |     |       30 |       7 | 2.86 |     | 50       | 3       | 1.22 |
|       11 |       1 | 0.41 |     |       31 |       9 | 3.67 |     | 51       | 7       | 2.86 |
|       12 |       2 | 0.82 |     |       32 |       5 | 2.04 |     | 52       | 6       | 2.45 |
|       13 |       3 | 1.22 |     |       33 |       6 | 2.45 |     | 53       | 6       | 2.45 |
|       14 |       3 | 1.22 |     |       34 |       9 | 3.67 |     | 54       | 4       | 1.63 |
|       15 |       3 | 1.22 |     |       35 |       4 | 1.63 |     | 55       | 5       | 2.04 |
|       16 |       4 | 1.63 |     |       36 |       6 | 2.45 |     |          |         |      |
|       17 |       5 | 2.04 |     |       37 |       2 | 0.82 |     |          |         |      |
|       18 |       5 | 2.04 |     |       38 |       2 | 0.82 |     |          |         |      |
|       19 |       7 | 2.86 |     |       39 |       4 | 1.63 |     |          |         |      |
|       20 |       3 | 1.22 |     |       40 |       5 | 2.04 |     |          |         |      |



### ⚖️ [6/55] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 418        | 33.57     |
| 2:4                  | 311        | 24.98     |
| 4:2                  | 295        | 23.69     |
| 5:1                  | 117        | 9.40      |
| 1:5                  | 77         | 6.18      |
| 6:0                  | 20         | 1.61      |
| 0:6                  | 7          | 0.56      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 5          | 55.56     |
| 5:1                  | 2          | 22.22     |
| 2:4                  | 1          | 11.11     |
| 4:2                  | 1          | 11.11     |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 8          | 36.36     |
| 2:4                  | 7          | 31.82     |
| 5:1                  | 3          | 13.64     |
| 4:2                  | 3          | 13.64     |
| 1:5                  | 1          | 4.55      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 12         | 34.29     |
| 2:4                  | 10         | 28.57     |
| 4:2                  | 6          | 17.14     |
| 5:1                  | 4          | 11.43     |
| 1:5                  | 3          | 8.57      |


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
| 2025-09-19 | 01408 | [4, 6, 17, 18, 28, 41]   |      0 | 2025-09-19 21:19:53.906114 |
| 2025-09-17 | 01407 | [11, 23, 25, 35, 38, 45] |      0 | 2025-09-17 18:47:42.209975 |
| 2025-09-14 | 01406 | [3, 6, 9, 10, 30, 37]    |      0 | 2025-09-15 21:15:13.139917 |
| 2025-09-12 | 01405 | [17, 22, 24, 37, 42, 43] |      0 | 2025-09-12 21:43:38.569616 |
| 2025-09-10 | 01404 | [7, 10, 18, 20, 24, 36]  |      0 | 2025-09-12 21:43:38.569702 |
| 2025-09-07 | 01403 | [6, 29, 30, 39, 42, 44]  |      0 | 2025-09-12 21:43:38.569781 |
| 2025-09-05 | 01402 | [1, 10, 20, 22, 41, 43]  |      0 | 2025-09-12 21:43:38.569856 |
| 2025-09-03 | 01401 | [14, 21, 23, 28, 44, 45] |      0 | 2025-09-12 21:43:38.569930 |
| 2025-08-31 | 01400 | [3, 4, 14, 30, 32, 38]   |      0 | 2025-09-02 17:20:47.544748 |
| 2025-08-29 | 01399 | [2, 4, 10, 24, 35, 36]   |      0 | 2025-08-30 10:11:45.760729 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     187 | 2.21 |     |       21 |     181 | 2.14 |     | 41       | 190     | 2.25 |
|        2 |     177 | 2.1  |     |       22 |     200 | 2.37 |     | 42       | 178     | 2.11 |
|        3 |     172 | 2.04 |     |       23 |     187 | 2.21 |     | 43       | 173     | 2.05 |
|        4 |     199 | 2.36 |     |       24 |     210 | 2.49 |     | 44       | 204     | 2.41 |
|        5 |     198 | 2.34 |     |       25 |     193 | 2.28 |     | 45       | 185     | 2.19 |
|        6 |     192 | 2.27 |     |       26 |     186 | 2.2  |     |          |         |      |
|        7 |     203 | 2.4  |     |       27 |     194 | 2.3  |     |          |         |      |
|        8 |     186 | 2.2  |     |       28 |     197 | 2.33 |     |          |         |      |
|        9 |     181 | 2.14 |     |       29 |     189 | 2.24 |     |          |         |      |
|       10 |     208 | 2.46 |     |       30 |     198 | 2.34 |     |          |         |      |
|       11 |     194 | 2.3  |     |       31 |     184 | 2.18 |     |          |         |      |
|       12 |     171 | 2.02 |     |       32 |     179 | 2.12 |     |          |         |      |
|       13 |     193 | 2.28 |     |       33 |     187 | 2.21 |     |          |         |      |
|       14 |     182 | 2.15 |     |       34 |     186 | 2.2  |     |          |         |      |
|       15 |     173 | 2.05 |     |       35 |     192 | 2.27 |     |          |         |      |
|       16 |     189 | 2.24 |     |       36 |     173 | 2.05 |     |          |         |      |
|       17 |     170 | 2.01 |     |       37 |     207 | 2.45 |     |          |         |      |
|       18 |     185 | 2.19 |     |       38 |     160 | 1.89 |     |          |         |      |
|       19 |     207 | 2.45 |     |       39 |     174 | 2.06 |     |          |         |      |
|       20 |     196 | 2.32 |     |       40 |     178 | 2.11 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 1.85 |     | 32       | 1       | 1.85 |
|        3 |       2 | 3.7  |     | 35       | 1       | 1.85 |
|        4 |       2 | 3.7  |     | 36       | 1       | 1.85 |
|        6 |       3 | 5.56 |     | 37       | 2       | 3.7  |
|        7 |       1 | 1.85 |     | 38       | 2       | 3.7  |
|        9 |       1 | 1.85 |     | 39       | 1       | 1.85 |
|       10 |       3 | 5.56 |     | 41       | 2       | 3.7  |
|       11 |       1 | 1.85 |     | 42       | 2       | 3.7  |
|       14 |       2 | 3.7  |     | 43       | 2       | 3.7  |
|       17 |       2 | 3.7  |     | 44       | 2       | 3.7  |
|       18 |       2 | 3.7  |     | 45       | 2       | 3.7  |
|       20 |       2 | 3.7  |     |          |         |      |
|       21 |       1 | 1.85 |     |          |         |      |
|       22 |       2 | 3.7  |     |          |         |      |
|       23 |       2 | 3.7  |     |          |         |      |
|       24 |       2 | 3.7  |     |          |         |      |
|       25 |       1 | 1.85 |     |          |         |      |
|       28 |       2 | 3.7  |     |          |         |      |
|       29 |       1 | 1.85 |     |          |         |      |
|       30 |       3 | 5.56 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.52 |     |       24 |       5 | 3.79 |     | 45       | 4       | 3.03 |
|        2 |       2 | 1.52 |     |       25 |       1 | 0.76 |     |          |         |      |
|        3 |       4 | 3.03 |     |       26 |       4 | 3.03 |     |          |         |      |
|        4 |       4 | 3.03 |     |       27 |       3 | 2.27 |     |          |         |      |
|        5 |       3 | 2.27 |     |       28 |       5 | 3.79 |     |          |         |      |
|        6 |       3 | 2.27 |     |       29 |       4 | 3.03 |     |          |         |      |
|        7 |       1 | 0.76 |     |       30 |       5 | 3.79 |     |          |         |      |
|        9 |       4 | 3.03 |     |       31 |       3 | 2.27 |     |          |         |      |
|       10 |       6 | 4.55 |     |       32 |       3 | 2.27 |     |          |         |      |
|       11 |       3 | 2.27 |     |       34 |       1 | 0.76 |     |          |         |      |
|       12 |       1 | 0.76 |     |       35 |       4 | 3.03 |     |          |         |      |
|       13 |       2 | 1.52 |     |       36 |       4 | 3.03 |     |          |         |      |
|       14 |       4 | 3.03 |     |       37 |       4 | 3.03 |     |          |         |      |
|       15 |       2 | 1.52 |     |       38 |       5 | 3.79 |     |          |         |      |
|       17 |       3 | 2.27 |     |       39 |       3 | 2.27 |     |          |         |      |
|       18 |       4 | 3.03 |     |       40 |       1 | 0.76 |     |          |         |      |
|       20 |       4 | 3.03 |     |       41 |       2 | 1.52 |     |          |         |      |
|       21 |       2 | 1.52 |     |       42 |       5 | 3.79 |     |          |         |      |
|       22 |       3 | 2.27 |     |       43 |       5 | 3.79 |     |          |         |      |
|       23 |       2 | 1.52 |     |       44 |       2 | 1.52 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.43 |     |       21 |       5 | 2.38 |     | 41       | 4       | 1.9  |
|        2 |       3 | 1.43 |     |       22 |       6 | 2.86 |     | 42       | 8       | 3.81 |
|        3 |       5 | 2.38 |     |       23 |       3 | 1.43 |     | 43       | 6       | 2.86 |
|        4 |       4 | 1.9  |     |       24 |       8 | 3.81 |     | 44       | 4       | 1.9  |
|        5 |       4 | 1.9  |     |       25 |       1 | 0.48 |     | 45       | 9       | 4.29 |
|        6 |       5 | 2.38 |     |       26 |       6 | 2.86 |     |          |         |      |
|        7 |       4 | 1.9  |     |       27 |       5 | 2.38 |     |          |         |      |
|        8 |       2 | 0.95 |     |       28 |       7 | 3.33 |     |          |         |      |
|        9 |       7 | 3.33 |     |       29 |       6 | 2.86 |     |          |         |      |
|       10 |       6 | 2.86 |     |       30 |       7 | 3.33 |     |          |         |      |
|       11 |       6 | 2.86 |     |       31 |       3 | 1.43 |     |          |         |      |
|       12 |       3 | 1.43 |     |       32 |       5 | 2.38 |     |          |         |      |
|       13 |       4 | 1.9  |     |       33 |       1 | 0.48 |     |          |         |      |
|       14 |       6 | 2.86 |     |       34 |       4 | 1.9  |     |          |         |      |
|       15 |       2 | 0.95 |     |       35 |       6 | 2.86 |     |          |         |      |
|       16 |       2 | 0.95 |     |       36 |       6 | 2.86 |     |          |         |      |
|       17 |       4 | 1.9  |     |       37 |       6 | 2.86 |     |          |         |      |
|       18 |       4 | 1.9  |     |       38 |       6 | 2.86 |     |          |         |      |
|       19 |       1 | 0.48 |     |       39 |       5 | 2.38 |     |          |         |      |
|       20 |       7 | 3.33 |     |       40 |       1 | 0.48 |     |          |         |      |



### ⚖️ [6/45] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 493        | 35.01     |
| 4:2                  | 335        | 23.79     |
| 2:4                  | 308        | 21.88     |
| 5:1                  | 129        | 9.16      |
| 1:5                  | 108        | 7.67      |
| 6:0                  | 21         | 1.49      |
| 0:6                  | 14         | 0.99      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 4          | 44.44     |
| 2:4                  | 2          | 22.22     |
| 1:5                  | 2          | 22.22     |
| 5:1                  | 1          | 11.11     |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 10         | 45.45     |
| 2:4                  | 5          | 22.73     |
| 1:5                  | 3          | 13.64     |
| 5:1                  | 2          | 9.09      |
| 4:2                  | 2          | 9.09      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 13         | 37.14     |
| 2:4                  | 10         | 28.57     |
| 1:5                  | 4          | 11.43     |
| 4:2                  | 4          | 11.43     |
| 5:1                  | 3          | 8.57      |
| 6:0                  | 1          | 2.86      |


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

