# Washington State Electric Vehicle (EV) Ecosystem Analysis
### Task 3: Real-World Dataset Analysis | Machine Learning Engineer Internship

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-4C72B0?style=flat)](https://seaborn.pydata.org/)
[![Scipy](https://img.shields.io/badge/Scipy-1.10+-8CAAE6?style=flat&logo=scipy&logoColor=white)](https://scipy.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)]()

---

## 📌 Executive Overview

This repository contains an end-to-end, empirical data analytics and machine learning foundation study investigating the **Washington State Electric Vehicle (EV) Population Dataset** (Department of Licensing).

The project is architected across a **modular 3-stage pipeline**:
1. **Data Hygiene & Domain Feature Engineering**
2. **Exploratory Data Analysis, Distribution Modeling & Statistical Hypothesis Testing**
3. **Market Concentration Modeling (HHI / CR4) & Strategic Infrastructure Insights**

The primary objective is to evaluate longitudinal market growth, automaker market concentration, technological autonomy divergence between pure **Battery Electric Vehicles (BEVs)** and **Plug-in Hybrid Electric Vehicles (PHEVs)**, and utility grid stress across Washington counties.

---

## 📊 Key Analytical Findings & Core Metrics Scorecard

| Metric Dimension | Empirical Quantitative Value | Strategic & Economic Interpretation |
| :--- | :--- | :--- |
| **Analyzed Fleet Size** | **150,000+ Units** | Sanitized modern commercial EV fleet (Model Years 2011–2024). |
| **Powertrain Breakdown** | **BEV: 77.7% (~117k) \| PHEV: 22.3% (~33.6k)** | Overwhelming market preference for zero-tailpipe emission platforms. |
| **Market Concentration (HHI)** | **2,353.0 Points** | Classified as a **"Highly Concentrated" Oligopoly** under DOJ/FTC antitrust criteria ($HHI > 1,800$). |
| **Four-Firm Dominance (CR4)** | **68.1% Market Dominance** | Top 4 automakers (Tesla, Nissan, Chevrolet, Ford) control over two-thirds of the fleet. |
| **Market Leader (Tesla)** | **46.0% Fleet Share (~69,000 units)** | Significant single-firm dominance backed by proprietary charging infrastructure. |
| **BEV Certified Autonomy** | **Median: 215.0 Miles** (IQR: 125.0–238.0 mi) | Robust intercity highway capability exceeding standard range thresholds. |
| **PHEV Certified Autonomy** | **Median: 26.0–30.0 Miles** (IQR: 20.0–38.0 mi) | Localized suburban commuting profile with internal combustion backup. |
| **Statistical Test (Mann-Whitney U)** | **$U = 4.82 \times 10^7, p < 10^{-15}$** | Rejects $H_0$; confirms statistically significant autonomy divergence. |
| **Primary Geographic Center** | **King County: 52.4% (79,000+ units)** | Pronounced spatial concentration within the Seattle economic corridor. |

---

## 📁 Repository Architecture

```text
├── data/
│   ├── Electric_Vehicle_Population_Data.csv   # Raw baseline dataset
│   └── ev_cleaned.csv                         # Sanitized & engineered analytical baseline
├── images/                                    # Publication-grade (300 DPI) visual assets
│   ├── 01_adoption_trend_by_years.png         # Model year growth trajectory (2011-2024)
│   ├── 02_top_10_manufacturers.png            # Fleet counts by top 10 automakers
│   ├── 03_ev_type_distribution.png            # BEV vs. PHEV total fleet volume
│   ├── 04_electric_range_distributions.png    # Certified range KDE and bimodal density
│   ├── 05_geographic_distribution.png         # Top 8 Washington counties by EV count
│   ├── 06_powertrain_era_transition.png       # Powertrain evolution across market eras
│   ├── 07_bev_vs_phev_range_comparison.png    # Comparative KDE density & range boxplots
│   ├── 08_manufacturer_range_dispersion.png   # Driving range spread across top 6 makes
│   ├── 09_battery_bracket_evolution.png       # Range category stacked shares by era
│   ├── 10_market_concentration_hhi.png        # Automaker market shares & HHI benchmark
│   ├── 11_utility_grid_demand.png             # Top electric utility charging loads
│   └── 12_top_municipalities_density.png      # Top 10 EV cities in Washington
├── notebooks/
│   ├── 01_data_cleaning_and_feature_engineering.ipynb
│   ├── 02_advanced_statistical_eda.ipynb
│   └── 03_market_dynamics_and_insights.ipynb
├── report/
│   ├── executive_summary_metrics.csv          # Consolidated quantitative scorecard
│   └── Task-3-Real-World-Dataset-Analysis.docx# Formal assessment submission report
├── README.md                                  # Comprehensive technical documentation
└── requirements.txt                           # Execution dependencies
```

---

## 🛠️ Pipeline Modules & Methodologies

### Module 01: Data Cleaning & Feature Engineering
* **Identifier Elimination:** Dropped zero-variance administrative columns (`vin_1_10`, `dol_vehicle_id`, `2020_census_tract`, and `vehicle_location`).
* **Text Normalization:** Standardized schema to `snake_case` and unified manufacturer text strings.
* **Engineered Attributes:**
  * `powertrain`: Binary segmentation into `BEV` and `PHEV`.
  * `adoption_era`: Divided into `Early Adoption (2011–2016)`, `Transition Phase (2017–2020)`, and `Mass Market (2021–Present)`.
  * `range_category`: Segmented certified range into `Short Range (<100 mi)`, `Mid Range (100–200 mi)`, and `Long Range (>200 mi)`.

### Module 02: Advanced Statistical EDA & Hypothesis Testing
* **Distribution Assessment:** Identified a bimodal range distribution via Kernel Density Estimation (KDE).
* **Hypothesis Testing (Mann-Whitney U Test):**
  * $H_0$: $\mu_{\text{BEV}} = \mu_{\text{PHEV}}$ (Driving ranges are identical).
  * $H_1$: $\mu_{\text{BEV}} > \mu_{\text{PHEV}}$ (BEV autonomy is significantly greater).
  * **Result:** $p\text{-value} < 10^{-15}$ (Strongly reject $H_0$).
* **Interquartile Range (IQR) Dispersion:** Evaluated battery technology spreads across top manufacturers (Tesla, Nissan, Chevrolet, BMW, Toyota, Ford).

### Module 03: Market Dynamics & Strategic Insights
* **Herfindahl-Hirschman Index (HHI):** Formulated as:
  $$HHI = \sum_{i=1}^{N} s_i^2$$
  Yielded **2,353.0 points**, demonstrating an oligopolistic market structure dominated by Tesla (46.0%).
* **Grid Demand Analysis:** Mapped fleet charging service distribution across utilities, demonstrating that **Puget Sound Energy** and **Seattle City Light** support over 70% of the state's EV load.

---

## 🚀 Installation & Reproduction Guide

### 1. Environment Setup
Clone the repository and create an isolated virtual environment:
```bash
git clone https://github.com/durgesh693/ev-population-analysis.git
cd ev-population-analysis

python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Required: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `python-docx`)*

### 3. Sequential Execution
Execute the modular notebooks in numerical sequence:
```bash
jupyter notebook notebooks/01_data_cleaning_and_feature_engineering.ipynb
jupyter notebook notebooks/02_advanced_statistical_eda.ipynb
jupyter notebook notebooks/03_market_dynamics_and_insights.ipynb
```

---

## 💡 Strategic Takeaways & Policy Recommendations

1. **Market De-Concentration Policies:** State rebate programs should prioritize entry-level non-luxury EVs ($<\$35,000$) from emerging manufacturers to balance Tesla's 46% market concentration.
2. **Targeted Substation Reinforcement:** Grid infrastructure investments must prioritize King and Snohomish counties, which account for over 63% of statewide registrations.
3. **Time-of-Use (TOU) Rate Mandates:** Utilities must implement automated off-peak charging tariffs to mitigate evening residential charging spikes.

---

## 👤 Author & Assessment Credits
* **Candidate Name:** Durgesh Maurya
* **Role:** Machine Learning Engineer Intern
* **Task:** Task 3 — Real-World Dataset Analysis Project
