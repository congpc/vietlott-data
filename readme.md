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
| Power 655 |          1257 | 2017-08-01   | 2025-10-18 |            1257 | 00001      | 01257       |
| Power 645 |          1421 | 2016-07-20   | 2025-10-19 |            1421 | 00001      | 01421       |
| Power 535 |           108 | 2025-06-29   | 2025-10-20 |             214 | 00001      | 00228       |
| Keno      |           343 | 2022-12-04   | 2025-09-30 |           44920 | #0110271   | #0254111    |
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

No significant matches found in backtest period.



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-10-18 | 01257 | [5, 16, 19, 21, 38, 43, 50]  |      0 | 2025-10-20 21:14:16.554776 |
| 2025-10-16 | 01256 | [14, 15, 24, 26, 27, 45, 36] |      0 | 2025-10-20 21:14:16.554885 |
| 2025-10-14 | 01255 | [8, 9, 16, 26, 37, 55, 12]   |      0 | 2025-10-14 18:48:17.226686 |
| 2025-10-11 | 01254 | [3, 7, 26, 43, 44, 46, 25]   |      0 | 2025-10-14 18:48:17.226834 |
| 2025-10-09 | 01253 | [7, 11, 21, 22, 39, 42, 40]  |      0 | 2025-10-14 18:48:17.226966 |
| 2025-10-07 | 01252 | [19, 22, 35, 37, 43, 45, 29] |      0 | 2025-10-08 21:40:23.214427 |
| 2025-10-04 | 01251 | [22, 33, 35, 36, 38, 40, 7]  |      0 | 2025-10-05 17:04:48.001158 |
| 2025-10-02 | 01250 | [1, 2, 20, 24, 27, 42, 43]   |      0 | 2025-10-05 17:04:48.001330 |
| 2025-09-30 | 01249 | [17, 23, 34, 39, 46, 52, 8]  |      0 | 2025-09-30 19:22:07.239312 |
| 2025-09-27 | 01248 | [8, 13, 19, 24, 39, 46, 1]   |      0 | 2025-09-30 19:22:07.239405 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     172 | 1.95 |     |       21 |     154 | 1.75 |     | 41       | 187     | 2.13 |
|        2 |     147 | 1.67 |     |       22 |     181 | 2.06 |     | 42       | 164     | 1.86 |
|        3 |     171 | 1.94 |     |       23 |     172 | 1.95 |     | 43       | 182     | 2.07 |
|        4 |     132 | 1.5  |     |       24 |     164 | 1.86 |     | 44       | 168     | 1.91 |
|        5 |     161 | 1.83 |     |       25 |     142 | 1.61 |     | 45       | 161     | 1.83 |
|        6 |     136 | 1.55 |     |       26 |     148 | 1.68 |     | 46       | 165     | 1.88 |
|        7 |     138 | 1.57 |     |       27 |     147 | 1.67 |     | 47       | 161     | 1.83 |
|        8 |     172 | 1.95 |     |       28 |     140 | 1.59 |     | 48       | 170     | 1.93 |
|        9 |     177 | 2.01 |     |       29 |     167 | 1.9  |     | 49       | 161     | 1.83 |
|       10 |     148 | 1.68 |     |       30 |     142 | 1.61 |     | 50       | 160     | 1.82 |
|       11 |     164 | 1.86 |     |       31 |     167 | 1.9  |     | 51       | 183     | 2.08 |
|       12 |     166 | 1.89 |     |       32 |     164 | 1.86 |     | 52       | 165     | 1.88 |
|       13 |     152 | 1.73 |     |       33 |     160 | 1.82 |     | 53       | 169     | 1.92 |
|       14 |     159 | 1.81 |     |       34 |     181 | 2.06 |     | 54       | 149     | 1.69 |
|       15 |     150 | 1.7  |     |       35 |     157 | 1.78 |     | 55       | 158     | 1.8  |
|       16 |     150 | 1.7  |     |       36 |     150 | 1.7  |     |          |         |      |
|       17 |     148 | 1.68 |     |       37 |     145 | 1.65 |     |          |         |      |
|       18 |     163 | 1.85 |     |       38 |     150 | 1.7  |     |          |         |      |
|       19 |     163 | 1.85 |     |       39 |     153 | 1.74 |     |          |         |      |
|       20 |     168 | 1.91 |     |       40 |     174 | 1.98 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       2 | 2.2  |     |       24 |       3 | 3.3  |     | 46       | 4       | 4.4 |
|        2 |       1 | 1.1  |     |       25 |       1 | 1.1  |     | 50       | 1       | 1.1 |
|        3 |       1 | 1.1  |     |       26 |       3 | 3.3  |     | 52       | 1       | 1.1 |
|        5 |       2 | 2.2  |     |       27 |       2 | 2.2  |     | 53       | 1       | 1.1 |
|        7 |       3 | 3.3  |     |       29 |       1 | 1.1  |     | 55       | 1       | 1.1 |
|        8 |       6 | 6.59 |     |       30 |       2 | 2.2  |     |          |         |     |
|        9 |       1 | 1.1  |     |       31 |       1 | 1.1  |     |          |         |     |
|       11 |       1 | 1.1  |     |       33 |       1 | 1.1  |     |          |         |     |
|       12 |       1 | 1.1  |     |       34 |       2 | 2.2  |     |          |         |     |
|       13 |       2 | 2.2  |     |       35 |       2 | 2.2  |     |          |         |     |
|       14 |       2 | 2.2  |     |       36 |       3 | 3.3  |     |          |         |     |
|       15 |       1 | 1.1  |     |       37 |       2 | 2.2  |     |          |         |     |
|       16 |       2 | 2.2  |     |       38 |       4 | 4.4  |     |          |         |     |
|       17 |       2 | 2.2  |     |       39 |       3 | 3.3  |     |          |         |     |
|       18 |       1 | 1.1  |     |       40 |       2 | 2.2  |     |          |         |     |
|       19 |       5 | 5.49 |     |       41 |       1 | 1.1  |     |          |         |     |
|       20 |       1 | 1.1  |     |       42 |       2 | 2.2  |     |          |         |     |
|       21 |       2 | 2.2  |     |       43 |       5 | 5.49 |     |          |         |     |
|       22 |       3 | 3.3  |     |       44 |       1 | 1.1  |     |          |         |     |
|       23 |       1 | 1.1  |     |       45 |       2 | 2.2  |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.65 |     |       23 |       2 | 1.1  |     | 44       | 5       | 2.75 |
|        2 |       5 | 2.75 |     |       24 |       5 | 2.75 |     | 45       | 3       | 1.65 |
|        3 |       2 | 1.1  |     |       25 |       2 | 1.1  |     | 46       | 5       | 2.75 |
|        5 |       4 | 2.2  |     |       26 |       4 | 2.2  |     | 48       | 1       | 0.55 |
|        6 |       2 | 1.1  |     |       27 |       4 | 2.2  |     | 49       | 2       | 1.1  |
|        7 |       4 | 2.2  |     |       28 |       2 | 1.1  |     | 50       | 3       | 1.65 |
|        8 |       7 | 3.85 |     |       29 |       1 | 0.55 |     | 51       | 2       | 1.1  |
|        9 |       6 | 3.3  |     |       30 |       6 | 3.3  |     | 52       | 4       | 2.2  |
|       11 |       2 | 1.1  |     |       31 |       3 | 1.65 |     | 53       | 3       | 1.65 |
|       12 |       1 | 0.55 |     |       33 |       2 | 1.1  |     | 55       | 4       | 2.2  |
|       13 |       3 | 1.65 |     |       34 |       5 | 2.75 |     |          |         |      |
|       14 |       2 | 1.1  |     |       35 |       4 | 2.2  |     |          |         |      |
|       15 |       2 | 1.1  |     |       36 |       3 | 1.65 |     |          |         |      |
|       16 |       5 | 2.75 |     |       37 |       2 | 1.1  |     |          |         |      |
|       17 |       5 | 2.75 |     |       38 |       6 | 3.3  |     |          |         |      |
|       18 |       2 | 1.1  |     |       39 |       4 | 2.2  |     |          |         |      |
|       19 |       9 | 4.95 |     |       40 |       5 | 2.75 |     |          |         |      |
|       20 |       3 | 1.65 |     |       41 |       2 | 1.1  |     |          |         |      |
|       21 |       3 | 1.65 |     |       42 |       4 | 2.2  |     |          |         |      |
|       22 |       6 | 3.3  |     |       43 |       8 | 4.4  |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 1.83 |     |       21 |       3 | 1.1  |     | 41       | 3       | 1.1  |
|        2 |       5 | 1.83 |     |       22 |       7 | 2.56 |     | 42       | 5       | 1.83 |
|        3 |       2 | 0.73 |     |       23 |       4 | 1.47 |     | 43       | 10      | 3.66 |
|        4 |       1 | 0.37 |     |       24 |       9 | 3.3  |     | 44       | 6       | 2.2  |
|        5 |       9 | 3.3  |     |       25 |       2 | 0.73 |     | 45       | 7       | 2.56 |
|        6 |       5 | 1.83 |     |       26 |       5 | 1.83 |     | 46       | 6       | 2.2  |
|        7 |       4 | 1.47 |     |       27 |       4 | 1.47 |     | 47       | 3       | 1.1  |
|        8 |       9 | 3.3  |     |       28 |       4 | 1.47 |     | 48       | 4       | 1.47 |
|        9 |       8 | 2.93 |     |       29 |       4 | 1.47 |     | 49       | 3       | 1.1  |
|       10 |       4 | 1.47 |     |       30 |       7 | 2.56 |     | 50       | 3       | 1.1  |
|       11 |       2 | 0.73 |     |       31 |       7 | 2.56 |     | 51       | 5       | 1.83 |
|       12 |       2 | 0.73 |     |       32 |       3 | 1.1  |     | 52       | 6       | 2.2  |
|       13 |       3 | 1.1  |     |       33 |       5 | 1.83 |     | 53       | 5       | 1.83 |
|       14 |       4 | 1.47 |     |       34 |       9 | 3.3  |     | 54       | 1       | 0.37 |
|       15 |       3 | 1.1  |     |       35 |       6 | 2.2  |     | 55       | 5       | 1.83 |
|       16 |       6 | 2.2  |     |       36 |       6 | 2.2  |     |          |         |      |
|       17 |       7 | 2.56 |     |       37 |       4 | 1.47 |     |          |         |      |
|       18 |       3 | 1.1  |     |       38 |       6 | 2.2  |     |          |         |      |
|       19 |      10 | 3.66 |     |       39 |       5 | 1.83 |     |          |         |      |
|       20 |       3 | 1.1  |     |       40 |       6 | 2.2  |     |          |         |      |



### ⚖️ [6/55] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 423        | 33.65     |
| 2:4                  | 314        | 24.98     |
| 4:2                  | 298        | 23.71     |
| 5:1                  | 118        | 9.39      |
| 1:5                  | 77         | 6.13      |
| 6:0                  | 20         | 1.59      |
| 0:6                  | 7          | 0.56      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 6          | 46.15     |
| 4:2                  | 3          | 23.08     |
| 2:4                  | 3          | 23.08     |
| 5:1                  | 1          | 7.69      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 10         | 38.46     |
| 2:4                  | 7          | 26.92     |
| 4:2                  | 4          | 15.38     |
| 5:1                  | 4          | 15.38     |
| 1:5                  | 1          | 3.85      |

### ⚖️ [6/55] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 15         | 38.46     |
| 2:4                  | 11         | 28.21     |
| 4:2                  | 8          | 20.51     |
| 5:1                  | 4          | 10.26     |
| 1:5                  | 1          | 2.56      |


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
| 2025-10-19 | 01421 | [16, 17, 25, 26, 28, 37] |      0 | 2025-10-20T21:14:22.712316 |
| 2025-10-17 | 01420 | [15, 17, 18, 26, 31, 42] |      0 | 2025-10-20T21:14:22.712418 |
| 2025-10-15 | 01419 | [1, 6, 18, 20, 29, 40]   |      0 | 2025-10-20T21:14:22.712513 |
| 2025-10-12 | 01418 | [4, 10, 16, 20, 28, 34]  |      0 | 2025-10-14 18:48:42.627700 |
| 2025-10-10 | 01417 | [4, 5, 25, 34, 39, 43]   |      0 | 2025-10-14 18:48:42.627800 |
| 2025-10-08 | 01416 | [8, 10, 11, 18, 23, 32]  |      0 | 2025-10-08 21:40:27.958251 |
| 2025-10-05 | 01415 | [5, 14, 22, 28, 32, 39]  |      0 | 2025-10-08 21:40:27.958348 |
| 2025-10-03 | 01414 | [29, 31, 32, 33, 34, 35] |      0 | 2025-10-05 17:05:12.128384 |
| 2025-10-01 | 01413 | [3, 6, 7, 19, 30, 35]    |      0 | 2025-10-05 17:05:12.128562 |
| 2025-09-28 | 01412 | [8, 13, 18, 26, 36, 39]  |      0 | 2025-09-30 19:22:37.845940 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     188 | 2.21 |     |       21 |     182 | 2.13 |     | 41       | 190     | 2.23 |
|        2 |     178 | 2.09 |     |       22 |     201 | 2.36 |     | 42       | 179     | 2.1  |
|        3 |     175 | 2.05 |     |       23 |     188 | 2.21 |     | 43       | 174     | 2.04 |
|        4 |     201 | 2.36 |     |       24 |     210 | 2.46 |     | 44       | 204     | 2.39 |
|        5 |     201 | 2.36 |     |       25 |     195 | 2.29 |     | 45       | 185     | 2.17 |
|        6 |     195 | 2.29 |     |       26 |     189 | 2.22 |     |          |         |      |
|        7 |     204 | 2.39 |     |       27 |     195 | 2.29 |     |          |         |      |
|        8 |     188 | 2.21 |     |       28 |     202 | 2.37 |     |          |         |      |
|        9 |     181 | 2.12 |     |       29 |     191 | 2.24 |     |          |         |      |
|       10 |     210 | 2.46 |     |       30 |     199 | 2.33 |     |          |         |      |
|       11 |     195 | 2.29 |     |       31 |     187 | 2.19 |     |          |         |      |
|       12 |     172 | 2.02 |     |       32 |     183 | 2.15 |     |          |         |      |
|       13 |     194 | 2.28 |     |       33 |     188 | 2.21 |     |          |         |      |
|       14 |     183 | 2.15 |     |       34 |     189 | 2.22 |     |          |         |      |
|       15 |     174 | 2.04 |     |       35 |     194 | 2.28 |     |          |         |      |
|       16 |     191 | 2.24 |     |       36 |     175 | 2.05 |     |          |         |      |
|       17 |     174 | 2.04 |     |       37 |     208 | 2.44 |     |          |         |      |
|       18 |     189 | 2.22 |     |       38 |     161 | 1.89 |     |          |         |      |
|       19 |     209 | 2.45 |     |       39 |     177 | 2.08 |     |          |         |      |
|       20 |     198 | 2.32 |     |       40 |     180 | 2.11 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |    % |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|
|        1 |       1 | 1.28 |     |       22 |       1 | 1.28 |
|        2 |       1 | 1.28 |     |       23 |       1 | 1.28 |
|        3 |       3 | 3.85 |     |       25 |       2 | 2.56 |
|        4 |       2 | 2.56 |     |       26 |       3 | 3.85 |
|        5 |       3 | 3.85 |     |       27 |       1 | 1.28 |
|        6 |       3 | 3.85 |     |       28 |       5 | 6.41 |
|        7 |       1 | 1.28 |     |       29 |       2 | 2.56 |
|        8 |       2 | 2.56 |     |       30 |       1 | 1.28 |
|       10 |       2 | 2.56 |     |       31 |       3 | 3.85 |
|       11 |       1 | 1.28 |     |       32 |       4 | 5.13 |
|       12 |       1 | 1.28 |     |       33 |       1 | 1.28 |
|       13 |       1 | 1.28 |     |       34 |       3 | 3.85 |
|       14 |       1 | 1.28 |     |       35 |       2 | 2.56 |
|       15 |       1 | 1.28 |     |       36 |       2 | 2.56 |
|       16 |       2 | 2.56 |     |       37 |       1 | 1.28 |
|       17 |       4 | 5.13 |     |       38 |       1 | 1.28 |
|       18 |       4 | 5.13 |     |       39 |       3 | 3.85 |
|       19 |       2 | 2.56 |     |       40 |       2 | 2.56 |
|       20 |       2 | 2.56 |     |       42 |       1 | 1.28 |
|       21 |       1 | 1.28 |     |       43 |       1 | 1.28 |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.92 |     |       21 |       2 | 1.28 |     | 41       | 2       | 1.28 |
|        2 |       3 | 1.92 |     |       22 |       3 | 1.92 |     | 42       | 4       | 2.56 |
|        3 |       6 | 3.85 |     |       23 |       3 | 1.92 |     | 43       | 4       | 2.56 |
|        4 |       5 | 3.21 |     |       24 |       3 | 1.92 |     | 44       | 2       | 1.28 |
|        5 |       3 | 1.92 |     |       25 |       3 | 1.92 |     | 45       | 2       | 1.28 |
|        6 |       6 | 3.85 |     |       26 |       3 | 1.92 |     |          |         |      |
|        7 |       2 | 1.28 |     |       27 |       1 | 0.64 |     |          |         |      |
|        8 |       2 | 1.28 |     |       28 |       8 | 5.13 |     |          |         |      |
|        9 |       3 | 1.92 |     |       29 |       3 | 1.92 |     |          |         |      |
|       10 |       7 | 4.49 |     |       30 |       4 | 2.56 |     |          |         |      |
|       11 |       3 | 1.92 |     |       31 |       3 | 1.92 |     |          |         |      |
|       12 |       1 | 0.64 |     |       32 |       6 | 3.85 |     |          |         |      |
|       13 |       2 | 1.28 |     |       33 |       1 | 0.64 |     |          |         |      |
|       14 |       3 | 1.92 |     |       34 |       3 | 1.92 |     |          |         |      |
|       15 |       1 | 0.64 |     |       35 |       4 | 2.56 |     |          |         |      |
|       16 |       2 | 1.28 |     |       36 |       4 | 2.56 |     |          |         |      |
|       17 |       6 | 3.85 |     |       37 |       4 | 2.56 |     |          |         |      |
|       18 |       7 | 4.49 |     |       38 |       3 | 1.92 |     |          |         |      |
|       19 |       2 | 1.28 |     |       39 |       6 | 3.85 |     |          |         |      |
|       20 |       5 | 3.21 |     |       40 |       3 | 1.92 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.71 |     |       21 |       3 | 1.28 |     | 41       | 2       | 0.85 |
|        2 |       4 | 1.71 |     |       22 |       4 | 1.71 |     | 42       | 6       | 2.56 |
|        3 |       8 | 3.42 |     |       23 |       3 | 1.28 |     | 43       | 6       | 2.56 |
|        4 |       6 | 2.56 |     |       24 |       6 | 2.56 |     | 44       | 3       | 1.28 |
|        5 |       6 | 2.56 |     |       25 |       3 | 1.28 |     | 45       | 5       | 2.14 |
|        6 |       7 | 2.99 |     |       26 |       9 | 3.85 |     |          |         |      |
|        7 |       2 | 0.85 |     |       27 |       5 | 2.14 |     |          |         |      |
|        8 |       2 | 0.85 |     |       28 |      10 | 4.27 |     |          |         |      |
|        9 |       5 | 2.14 |     |       29 |       7 | 2.99 |     |          |         |      |
|       10 |       8 | 3.42 |     |       30 |       7 | 2.99 |     |          |         |      |
|       11 |       4 | 1.71 |     |       31 |       6 | 2.56 |     |          |         |      |
|       12 |       3 | 1.28 |     |       32 |       8 | 3.42 |     |          |         |      |
|       13 |       3 | 1.28 |     |       33 |       1 | 0.43 |     |          |         |      |
|       14 |       5 | 2.14 |     |       34 |       6 | 2.56 |     |          |         |      |
|       15 |       3 | 1.28 |     |       35 |       7 | 2.99 |     |          |         |      |
|       16 |       3 | 1.28 |     |       36 |       6 | 2.56 |     |          |         |      |
|       17 |       7 | 2.99 |     |       37 |       6 | 2.56 |     |          |         |      |
|       18 |       8 | 3.42 |     |       38 |       7 | 2.99 |     |          |         |      |
|       19 |       2 | 0.85 |     |       39 |       8 | 3.42 |     |          |         |      |
|       20 |       7 | 2.99 |     |       40 |       3 | 1.28 |     |          |         |      |



### ⚖️ [6/45] Odd vs. Even Analysis (All Time)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 496        | 34.90     |
| 4:2                  | 339        | 23.86     |
| 2:4                  | 313        | 22.03     |
| 5:1                  | 129        | 9.08      |
| 1:5                  | 108        | 7.60      |
| 6:0                  | 21         | 1.48      |
| 0:6                  | 15         | 1.06      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 30 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 2:4                  | 5          | 38.46     |
| 4:2                  | 4          | 30.77     |
| 3:3                  | 3          | 23.08     |
| 0:6                  | 1          | 7.69      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 60 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 8          | 30.77     |
| 2:4                  | 8          | 30.77     |
| 4:2                  | 4          | 15.38     |
| 1:5                  | 3          | 11.54     |
| 5:1                  | 2          | 7.69      |
| 0:6                  | 1          | 3.85      |

### ⚖️ [6/45] Odd vs. Even Analysis (Last 90 Days)
| Split (Odd:Even)     | Count      | Ratio (%)  |
|:---------------------|:-----------|:-----------|
| 3:3                  | 13         | 33.33     |
| 2:4                  | 12         | 30.77     |
| 4:2                  | 6          | 15.38     |
| 1:5                  | 4          | 10.26     |
| 5:1                  | 3          | 7.69      |
| 0:6                  | 1          | 2.56      |


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

