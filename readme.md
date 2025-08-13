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
| Power 655 |          1228 | 2017-08-01   | 2025-08-12 |            1228 | 00001      | 01228       |
| Power 645 |          1391 | 2016-07-20   | 2025-08-10 |            1391 | 00001      | 01391       |
| Power 535 |            43 | 2025-06-29   | 2025-08-13 |              83 | 00001      | 00091       |
| Keno      |           117 | 2022-12-04   | 2025-08-13 |           18161 | #0110271   | #0248459    |
| 3D        |           962 | 2019-04-22   | 2025-08-11 |             962 | 00001      | 00962       |
| 3D Pro    |           609 | 2021-09-14   | 2025-08-12 |             609 | 00001      | 00609       |
| Bingo18   |           254 | 2024-12-03   | 2025-08-13 |           40230 | 0083123    | 0123358     |

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
| 2025-08-12 | 01228 | [1, 6, 24, 37, 40, 55, 10]   |      0 | 2025-08-13 15:14:09.192985 |
| 2025-08-09 | 01227 | [5, 9, 16, 36, 43, 51, 19]   |      0 | 2025-08-13 15:14:09.193064 |
| 2025-08-07 | 01226 | [6, 24, 31, 32, 39, 48, 52]  |      0 | 2025-08-13 15:14:09.193102 |
| 2025-08-05 | 01225 | [8, 41, 45, 51, 52, 53, 31]  |      0 | 2025-08-13 15:14:09.193136 |
| 2025-08-02 | 01224 | [12, 24, 29, 33, 34, 35, 47] |      0 | 2025-08-13 15:14:09.193169 |
| 2025-07-31 | 01223 | [5, 17, 31, 42, 46, 49, 37]  |      0 | 2025-08-01 00:00:35.635172 |
| 2025-07-29 | 01222 | [4, 8, 23, 43, 45, 51, 48]   |      0 | 2025-07-30 00:00:36.365372 |
| 2025-07-26 | 01221 | [5, 26, 28, 29, 33, 54, 34]  |      0 | 2025-07-27 00:00:32.385732 |
| 2025-07-24 | 01220 | [5, 10, 24, 29, 30, 34, 45]  |      0 | 2025-07-25 12:00:38.542614 |
| 2025-07-22 | 01219 | [9, 10, 15, 28, 33, 44, 22]  |      0 | 2025-07-23 00:01:21.445784 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     168 | 1.95 |     |       21 |     151 | 1.76 |     | 41       | 185     | 2.15 |
|        2 |     142 | 1.65 |     |       22 |     175 | 2.04 |     | 42       | 160     | 1.86 |
|        3 |     169 | 1.97 |     |       23 |     169 | 1.97 |     | 43       | 174     | 2.02 |
|        4 |     132 | 1.54 |     |       24 |     159 | 1.85 |     | 44       | 163     | 1.9  |
|        5 |     156 | 1.82 |     |       25 |     140 | 1.63 |     | 45       | 157     | 1.83 |
|        6 |     133 | 1.55 |     |       26 |     144 | 1.68 |     | 46       | 160     | 1.86 |
|        7 |     134 | 1.56 |     |       27 |     143 | 1.66 |     | 47       | 159     | 1.85 |
|        8 |     165 | 1.92 |     |       28 |     138 | 1.61 |     | 48       | 168     | 1.95 |
|        9 |     171 | 1.99 |     |       29 |     166 | 1.93 |     | 49       | 159     | 1.85 |
|       10 |     147 | 1.71 |     |       30 |     136 | 1.58 |     | 50       | 157     | 1.83 |
|       11 |     162 | 1.88 |     |       31 |     163 | 1.9  |     | 51       | 181     | 2.11 |
|       12 |     165 | 1.92 |     |       32 |     162 | 1.88 |     | 52       | 161     | 1.87 |
|       13 |     149 | 1.73 |     |       33 |     158 | 1.84 |     | 53       | 165     | 1.92 |
|       14 |     155 | 1.8  |     |       34 |     175 | 2.04 |     | 54       | 149     | 1.73 |
|       15 |     148 | 1.72 |     |       35 |     152 | 1.77 |     | 55       | 154     | 1.79 |
|       16 |     145 | 1.69 |     |       36 |     145 | 1.69 |     |          |         |      |
|       17 |     142 | 1.65 |     |       37 |     143 | 1.66 |     |          |         |      |
|       18 |     160 | 1.86 |     |       38 |     144 | 1.68 |     |          |         |      |
|       19 |     154 | 1.79 |     |       39 |     149 | 1.73 |     |          |         |      |
|       20 |     165 | 1.92 |     |       40 |     169 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |   % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       1 | 1.1 |     |       29 |       3 | 3.3 |     | 51       | 3       | 3.3 |
|        4 |       1 | 1.1 |     |       30 |       2 | 2.2 |     | 52       | 2       | 2.2 |
|        5 |       4 | 4.4 |     |       31 |       4 | 4.4 |     | 53       | 2       | 2.2 |
|        6 |       2 | 2.2 |     |       32 |       2 | 2.2 |     | 54       | 2       | 2.2 |
|        8 |       3 | 3.3 |     |       33 |       4 | 4.4 |     | 55       | 1       | 1.1 |
|        9 |       3 | 3.3 |     |       34 |       3 | 3.3 |     |          |         |     |
|       10 |       3 | 3.3 |     |       35 |       1 | 1.1 |     |          |         |     |
|       12 |       1 | 1.1 |     |       36 |       3 | 3.3 |     |          |         |     |
|       13 |       1 | 1.1 |     |       37 |       2 | 2.2 |     |          |         |     |
|       15 |       1 | 1.1 |     |       39 |       2 | 2.2 |     |          |         |     |
|       16 |       1 | 1.1 |     |       40 |       2 | 2.2 |     |          |         |     |
|       17 |       1 | 1.1 |     |       41 |       1 | 1.1 |     |          |         |     |
|       18 |       2 | 2.2 |     |       42 |       1 | 1.1 |     |          |         |     |
|       19 |       1 | 1.1 |     |       43 |       2 | 2.2 |     |          |         |     |
|       20 |       1 | 1.1 |     |       44 |       2 | 2.2 |     |          |         |     |
|       22 |       1 | 1.1 |     |       45 |       3 | 3.3 |     |          |         |     |
|       23 |       1 | 1.1 |     |       46 |       1 | 1.1 |     |          |         |     |
|       24 |       4 | 4.4 |     |       47 |       1 | 1.1 |     |          |         |     |
|       26 |       2 | 2.2 |     |       48 |       4 | 4.4 |     |          |         |     |
|       28 |       3 | 3.3 |     |       49 |       1 | 1.1 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.1  |     |       22 |       4 | 2.2  |     | 43       | 4       | 2.2  |
|        2 |       2 | 1.1  |     |       23 |       2 | 1.1  |     | 44       | 5       | 2.75 |
|        3 |       5 | 2.75 |     |       24 |       6 | 3.3  |     | 45       | 7       | 3.85 |
|        4 |       1 | 0.55 |     |       25 |       1 | 0.55 |     | 46       | 1       | 0.55 |
|        5 |       5 | 2.75 |     |       26 |       3 | 1.65 |     | 47       | 3       | 1.65 |
|        6 |       3 | 1.65 |     |       27 |       3 | 1.65 |     | 48       | 6       | 3.3  |
|        7 |       1 | 0.55 |     |       28 |       3 | 1.65 |     | 49       | 1       | 0.55 |
|        8 |       4 | 2.2  |     |       29 |       4 | 2.2  |     | 50       | 2       | 1.1  |
|        9 |       5 | 2.75 |     |       30 |       3 | 1.65 |     | 51       | 6       | 3.3  |
|       10 |       5 | 2.75 |     |       31 |       6 | 3.3  |     | 52       | 3       | 1.65 |
|       11 |       3 | 1.65 |     |       32 |       5 | 2.75 |     | 53       | 5       | 2.75 |
|       12 |       4 | 2.2  |     |       33 |       6 | 3.3  |     | 54       | 4       | 2.2  |
|       13 |       3 | 1.65 |     |       34 |       6 | 3.3  |     | 55       | 2       | 1.1  |
|       14 |       2 | 1.1  |     |       35 |       1 | 0.55 |     |          |         |      |
|       15 |       4 | 2.2  |     |       36 |       3 | 1.65 |     |          |         |      |
|       16 |       3 | 1.65 |     |       37 |       2 | 1.1  |     |          |         |      |
|       17 |       1 | 0.55 |     |       39 |       3 | 1.65 |     |          |         |      |
|       18 |       5 | 2.75 |     |       40 |       3 | 1.65 |     |          |         |      |
|       19 |       2 | 1.1  |     |       41 |       3 | 1.65 |     |          |         |      |
|       20 |       3 | 1.65 |     |       42 |       3 | 1.65 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 0.73 |     |       21 |       3 | 1.1  |     | 41       | 7       | 2.56 |
|        2 |       4 | 1.47 |     |       22 |       5 | 1.83 |     | 42       | 5       | 1.83 |
|        3 |       7 | 2.56 |     |       23 |       2 | 0.73 |     | 43       | 5       | 1.83 |
|        4 |       2 | 0.73 |     |       24 |       7 | 2.56 |     | 44       | 9       | 3.3  |
|        5 |       5 | 1.83 |     |       25 |       1 | 0.37 |     | 45       | 12      | 4.4  |
|        6 |       7 | 2.56 |     |       26 |       4 | 1.47 |     | 46       | 4       | 1.47 |
|        7 |       2 | 0.73 |     |       27 |       6 | 2.2  |     | 47       | 6       | 2.2  |
|        8 |       6 | 2.2  |     |       28 |       3 | 1.1  |     | 48       | 8       | 2.93 |
|        9 |       8 | 2.93 |     |       29 |       6 | 2.2  |     | 49       | 4       | 1.47 |
|       10 |       5 | 1.83 |     |       30 |       4 | 1.47 |     | 50       | 4       | 1.47 |
|       11 |       4 | 1.47 |     |       31 |       6 | 2.2  |     | 51       | 7       | 2.56 |
|       12 |       6 | 2.2  |     |       32 |       5 | 1.83 |     | 52       | 5       | 1.83 |
|       13 |       4 | 1.47 |     |       33 |       7 | 2.56 |     | 53       | 5       | 1.83 |
|       14 |       6 | 2.2  |     |       34 |       8 | 2.93 |     | 54       | 5       | 1.83 |
|       15 |       6 | 2.2  |     |       35 |       1 | 0.37 |     | 55       | 5       | 1.83 |
|       16 |       5 | 1.83 |     |       36 |       3 | 1.1  |     |          |         |      |
|       17 |       3 | 1.1  |     |       37 |       5 | 1.83 |     |          |         |      |
|       18 |       7 | 2.56 |     |       38 |       1 | 0.37 |     |          |         |      |
|       19 |       5 | 1.83 |     |       39 |       3 | 1.1  |     |          |         |      |
|       20 |       4 | 1.47 |     |       40 |       4 | 1.47 |     |          |         |      |



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
| 2025-08-10 | 01391 | [13, 21, 26, 28, 31, 35] |      0 | 2025-08-13 14:28:12.808613 |
| 2025-08-08 | 01390 | [11, 17, 20, 26, 27, 38] |      0 | 2025-08-13 14:28:12.808767 |
| 2025-08-06 | 01389 | [3, 12, 14, 18, 29, 34]  |      0 | 2025-08-13 14:28:12.808870 |
| 2025-08-03 | 01388 | [5, 14, 24, 26, 37, 43]  |      0 | 2025-08-13 14:28:12.808979 |
| 2025-08-01 | 01387 | [5, 29, 30, 31, 36, 38]  |      0 | 2025-08-13 14:28:12.809068 |
| 2025-07-30 | 01386 | [2, 3, 6, 16, 26, 34]    |      0 | 2025-07-31 00:00:49.595399 |
| 2025-07-27 | 01385 | [1, 9, 12, 27, 39, 45]   |      0 | 2025-07-28 00:00:47.866257 |
| 2025-07-25 | 01384 | [20, 30, 34, 35, 38, 39] |      0 | 2025-07-26 00:00:50.423814 |
| 2025-07-23 | 01383 | [24, 26, 29, 32, 37, 44] |      0 | 2025-07-24 00:01:57.974437 |
| 2025-07-20 | 01382 | [11, 13, 14, 20, 37, 42] |      0 | 2025-07-21 00:01:46.476037 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     185 | 2.22 |     |       21 |     180 | 2.16 |     | 41       | 188     | 2.25 |
|        2 |     175 | 2.1  |     |       22 |     197 | 2.36 |     | 42       | 173     | 2.07 |
|        3 |     169 | 2.02 |     |       23 |     185 | 2.22 |     | 43       | 169     | 2.02 |
|        4 |     195 | 2.34 |     |       24 |     206 | 2.47 |     | 44       | 202     | 2.42 |
|        5 |     197 | 2.36 |     |       25 |     192 | 2.3  |     | 45       | 181     | 2.17 |
|        6 |     189 | 2.26 |     |       26 |     185 | 2.22 |     |          |         |      |
|        7 |     202 | 2.42 |     |       27 |     192 | 2.3  |     |          |         |      |
|        8 |     186 | 2.23 |     |       28 |     193 | 2.31 |     |          |         |      |
|        9 |     177 | 2.12 |     |       29 |     187 | 2.24 |     |          |         |      |
|       10 |     202 | 2.42 |     |       30 |     194 | 2.32 |     |          |         |      |
|       11 |     192 | 2.3  |     |       31 |     183 | 2.19 |     |          |         |      |
|       12 |     171 | 2.05 |     |       32 |     176 | 2.11 |     |          |         |      |
|       13 |     192 | 2.3  |     |       33 |     187 | 2.24 |     |          |         |      |
|       14 |     180 | 2.16 |     |       34 |     186 | 2.23 |     |          |         |      |
|       15 |     171 | 2.05 |     |       35 |     189 | 2.26 |     |          |         |      |
|       16 |     189 | 2.26 |     |       36 |     170 | 2.04 |     |          |         |      |
|       17 |     168 | 2.01 |     |       37 |     204 | 2.44 |     |          |         |      |
|       18 |     182 | 2.18 |     |       38 |     157 | 1.88 |     |          |         |      |
|       19 |     207 | 2.48 |     |       39 |     171 | 2.05 |     |          |         |      |
|       20 |     193 | 2.31 |     |       40 |     177 | 2.12 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 1.39 |     | 27       | 2       | 2.78 |
|        2 |       1 | 1.39 |     | 28       | 2       | 2.78 |
|        3 |       2 | 2.78 |     | 29       | 3       | 4.17 |
|        5 |       2 | 2.78 |     | 30       | 2       | 2.78 |
|        6 |       2 | 2.78 |     | 31       | 2       | 2.78 |
|        7 |       1 | 1.39 |     | 32       | 1       | 1.39 |
|        9 |       1 | 1.39 |     | 34       | 3       | 4.17 |
|       11 |       3 | 4.17 |     | 35       | 2       | 2.78 |
|       12 |       2 | 2.78 |     | 36       | 1       | 1.39 |
|       13 |       2 | 2.78 |     | 37       | 3       | 4.17 |
|       14 |       4 | 5.56 |     | 38       | 3       | 4.17 |
|       16 |       1 | 1.39 |     | 39       | 2       | 2.78 |
|       17 |       1 | 1.39 |     | 42       | 3       | 4.17 |
|       18 |       1 | 1.39 |     | 43       | 1       | 1.39 |
|       19 |       1 | 1.39 |     | 44       | 1       | 1.39 |
|       20 |       3 | 4.17 |     | 45       | 2       | 2.78 |
|       21 |       2 | 2.78 |     |          |         |      |
|       22 |       1 | 1.39 |     |          |         |      |
|       24 |       3 | 4.17 |     |          |         |      |
|       26 |       5 | 6.94 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.33 |     |       22 |       5 | 3.33 |     | 43       | 2       | 1.33 |
|        2 |       2 | 1.33 |     |       23 |       4 | 2.67 |     | 44       | 3       | 2.0  |
|        3 |       2 | 1.33 |     |       24 |       5 | 3.33 |     | 45       | 6       | 4.0  |
|        5 |       3 | 2    |     |       25 |       1 | 0.67 |     |          |         |      |
|        6 |       2 | 1.33 |     |       26 |      10 | 6.67 |     |          |         |      |
|        7 |       3 | 2    |     |       27 |       4 | 2.67 |     |          |         |      |
|        8 |       4 | 2.67 |     |       28 |       4 | 2.67 |     |          |         |      |
|        9 |       5 | 3.33 |     |       29 |       7 | 4.67 |     |          |         |      |
|       10 |       2 | 1.33 |     |       30 |       4 | 2.67 |     |          |         |      |
|       11 |       4 | 2.67 |     |       31 |       2 | 1.33 |     |          |         |      |
|       12 |       3 | 2    |     |       32 |       3 | 2    |     |          |         |      |
|       13 |       3 | 2    |     |       33 |       1 | 0.67 |     |          |         |      |
|       14 |       6 | 4    |     |       34 |       5 | 3.33 |     |          |         |      |
|       15 |       1 | 0.67 |     |       35 |       4 | 2.67 |     |          |         |      |
|       16 |       3 | 2    |     |       36 |       4 | 2.67 |     |          |         |      |
|       17 |       2 | 1.33 |     |       37 |       3 | 2    |     |          |         |      |
|       18 |       2 | 1.33 |     |       38 |       3 | 2    |     |          |         |      |
|       19 |       2 | 1.33 |     |       39 |       3 | 2    |     |          |         |      |
|       20 |       5 | 3.33 |     |       41 |       4 | 2.67 |     |          |         |      |
|       21 |       4 | 2.67 |     |       42 |       3 | 2    |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.32 |     |       21 |       5 | 2.19 |     | 42       | 5       | 2.19 |
|        2 |       4 | 1.75 |     |       22 |       8 | 3.51 |     | 43       | 3       | 1.32 |
|        3 |       2 | 0.88 |     |       23 |       7 | 3.07 |     | 44       | 6       | 2.63 |
|        4 |       2 | 0.88 |     |       24 |       9 | 3.95 |     | 45       | 8       | 3.51 |
|        5 |       5 | 2.19 |     |       25 |       1 | 0.44 |     |          |         |      |
|        6 |       4 | 1.75 |     |       26 |      12 | 5.26 |     |          |         |      |
|        7 |       5 | 2.19 |     |       27 |       7 | 3.07 |     |          |         |      |
|        8 |       4 | 1.75 |     |       28 |       7 | 3.07 |     |          |         |      |
|        9 |       7 | 3.07 |     |       29 |      10 | 4.39 |     |          |         |      |
|       10 |       3 | 1.32 |     |       30 |       7 | 3.07 |     |          |         |      |
|       11 |       5 | 2.19 |     |       31 |       4 | 1.75 |     |          |         |      |
|       12 |       4 | 1.75 |     |       32 |       5 | 2.19 |     |          |         |      |
|       13 |       6 | 2.63 |     |       33 |       1 | 0.44 |     |          |         |      |
|       14 |       9 | 3.95 |     |       34 |       5 | 2.19 |     |          |         |      |
|       15 |       2 | 0.88 |     |       35 |       6 | 2.63 |     |          |         |      |
|       16 |       4 | 1.75 |     |       36 |       5 | 2.19 |     |          |         |      |
|       17 |       5 | 2.19 |     |       37 |       6 | 2.63 |     |          |         |      |
|       18 |       3 | 1.32 |     |       38 |       3 | 1.32 |     |          |         |      |
|       19 |       4 | 1.75 |     |       39 |       4 | 1.75 |     |          |         |      |
|       20 |       5 | 2.19 |     |       41 |       8 | 3.51 |     |          |         |      |



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

