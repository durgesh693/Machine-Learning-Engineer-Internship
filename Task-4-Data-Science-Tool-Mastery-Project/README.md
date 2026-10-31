# 🛒 E-Commerce Customer Churn Prediction & Retention Engine

Production-grade Machine Learning pipeline aur serving system jo e-commerce customers ke churn hone ke risk ko early-stage behavioral signals, cart friction, aur engagement telemetry ke through accurately predict karta hai.

---

## 📌 Project Overview & Business Value

* **Business Problem:** E-commerce platforms me customer acquisition cost (CAC) retention cost se kafi zyada hoti hai. Churn hone se pehle dormant aur frustrated customers ko identify karna zaroori hai taaki pro-active discount ya personalized outreach trigger ki ja sake.
* **Core Challenge:** Class imbalance (~29% churners vs ~71% retained) aur non-informative demographic columns jo model me variance aur overfitting add karte hain.
* **Architecture:** Scikit-Learn pipelines ke through leakage-free preprocessing, balanced LightGBM classification, aur production serving ke liye asynchronous FastAPI service with Jinja2 interactive UI.

---

## 📊 Model Evaluation & Benchmarks

Model ko standard accuracy ki jagah imbalanced classification ke true metrics—**PR-AUC (Average Precision)** aur **ROC-AUC**—par evaluate kiya gaya hai:

| Metric | Logistic Regression (Baseline) | LightGBM Classifier (Production) | Relative Improvement |
| :--- | :---: | :---: | :---: |
| **ROC-AUC** | 0.7996 | **0.9029** | **+12.9%** |
| **PR-AUC (Average Precision)** | 0.6419 | **0.8660** | **+34.9%** |
| **Precision (Churn Class 1)** | 53.46% | **78.44%** | **+46.7%** |
| **Recall (Churn Class 1)** | 72.11% | **77.54%** | **+7.5%** |
| **F1-Score (Churn Class 1)** | 0.6140 | **0.7799** | **+27.0%** |
| **Overall Accuracy** | 73.80% | **87.35%** | **+18.4%** |

---

## ⚙️ Engineering Decisions & Methodology

### 1. Empirical Feature Selection
* **Dropped Demographic Noise:** `Country`, `City`, `Gender`, `Age`, aur `Signup_Quarter` ko drop kiya gaya kyunki inka correlation churn ke sath flat/noisy tha aur high cardinality overfitting cause kar rahi thi.
* **Collinear Telemetry Elimination:** Raw features (`Session_Duration_Avg`, `Pages_Per_Session`, `Mobile_App_Usage`, `Login_Frequency`, `Email_Open_Rate`) ko retain karne ki jagah domain-driven composites me condense kiya gaya.

### 2. Domain-Driven Feature Engineering
* **`Digital_Engagement_Composite`**: App usage, login frequency, aur email opens ka weighted score ($0.4 \times App + 0.3 \times Email + 0.3 \times Login$).
* **`Engagement_Friction_Ratio`**: Telemetry interaction rate vs cart drops/customer calls ka ratio.
* **`High_Cart_Friction`**: Binary threshold flag jo persistent cart drop-offs ko isolate karta hai.
* **`Is_Dormant_90Days`**: Recency cut-off rule jo `Days_Since_Last_Purchase > 90` hone par inactive state detect karta hai.
* **`Annual_Monetary_Velocity` & `Spend_Per_Purchase`**: Customer transactional value aur spending rate ka velocity metric.

### 3. Leakage-Free Preprocessing Pipeline
* Scikit-Learn `Pipeline` framework ka use karke training aur validation partitions ke beech zero information leakage ensure ki gayi.
* Imbalanced target class ko handle karne ke liye tree-level loss adjustments (`class_weight='balanced'`) use kiye gaye.

---

## 🗂️ Project Structure

```text
ecommerce-churn-prediction/
│
├── notebooks/
│   ├── 01_data_cleaning_and_validation.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_feature_engineering_and_selection.ipynb
│   └── 04_model_training_and_pipeline.ipynb
│
├── models/
│   └── churn_production_pipeline.joblib
│
├── templates/
│   └── index.html
│
├── .gitignore
├── app.py
├── requirements.txt
└── README.md


