# Machine Learning Engineer Internship — YuvaIntern

This repository contains the complete codebase, modular notebooks, and formal reports developed during the **8-Week Machine Learning Engineer / Data Scientist Internship** at **YuvaIntern**.

---

## 📂 Repository Structure

The repository follows a single-repo monorepo approach where each milestone/task is maintained in an independent, modular subfolder:

```text
Machine-Learning-Engineer-Internship/
└── Task-1-Data-Science-Fundamentals/
    ├── 01-Python-Fundamentals/
    │   └── python_fundamentals.ipynb
    ├── 02-Statistics-Fundamentals/
    │   └── statistics_fundamentals.ipynb
    ├── 03-Data-Types/
    │   └── data_types.ipynb
    ├── 04-Data-Science-Concepts/
    │   └── data_science_concepts.ipynb
    ├── 05-Industry-Best-Practices/
    │   └── industry_best_practices.ipynb
    ├── 06-Practical-Assignment/
    │   └── practical_assignment.ipynb
    ├── report/
    │   └── Task-1-Data-Science-Fundamentals.docx
    └── README.md
```

---

## 📌 Task 1: Data Science Fundamentals Assessment

Task 1 establishes foundational competencies in programming, statistical mathematics, machine learning theory, and production best practices, paired with an end-to-end practical linear regression modeling assignment.

### 📚 Modules Overview

| Folder / Module | Focus Topics | Notebook |
| :--- | :--- | :--- |
| **01-Python-Fundamentals** | Variables, Control Flow, Functions, Data Structures, Exceptions, NumPy & Pandas Basics | `python_fundamentals.ipynb` |
| **02-Statistics-Fundamentals** | Mean, Median, Mode, Variance, Std Dev, Normal Distribution, Correlation, Hypothesis Testing | `statistics_fundamentals.ipynb` |
| **03-Data-Types** | Numerical, Categorical (Nominal/Ordinal), Boolean, Datetime, Missing Data Handling | `data_types.ipynb` |
| **04-Data-Science-Concepts** | End-to-End Pipeline, EDA, Feature Engineering, Train/Test Split, Overfitting vs Underfitting | `data_science_concepts.ipynb` |
| **05-Industry-Best-Practices** | Semantic Naming, Defensive Coding, Reproducibility, Train-Test Isolation, Git Hygiene | `industry_best_practices.ipynb` |
| **06-Practical-Assignment** | End-to-End Linear Regression: Data Generation → EDA → Model Fit → Evaluation → Predictions | `practical_assignment.ipynb` |

---

## 🧪 Practical Assignment Highlights (Module 06)

* **Objective:** Model and predict student exam scores using study duration.
* **Dataset:** 25 structured observations (`Hours_Studied`, `Previous_Score`, `Exam_Score`).
* **Model:** Ordinary Least Squares (OLS) Linear Regression (`Scikit-Learn`).
* **Train/Test Split:** 80% Training, 20% Unseen Testing (`random_state=42`).
* **Derived Formulation:**
  $$\text{Exam\_Score} = 6.42 \times \text{Hours\_Studied} + 39.11$$
* **Evaluation Metrics:**
  * **Mean Absolute Error (MAE):** $\approx 1.12$
  * **Mean Squared Error (MSE):** $\approx 1.85$
  * **Root Mean Squared Error (RMSE):** $\approx 1.36$
  * **$R^2$ Score:** $> 0.98$ (Strong explanatory power)

---

## ⚙️ Environment Setup & Installation

Follow these instructions to configure the identical environment locally using VS Code and Git Bash:

### 1. Clone the Repository
```bash
git clone https://github.com/<durgesh693 >/Machine-Learning-Engineer-Internship.git
cd Machine-Learning-Engineer-Internship/Task-1-Data-Science-Fundamentals
```

### 2. Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows (Git Bash)
source venv/Scripts/activate

# Activate on Linux/macOS
# source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install jupyter ipykernel numpy pandas matplotlib seaborn scipy scikit-learn
```

### 4. Register Custom Jupyter Kernel
```bash
python -m ipykernel install --user --name=ml-internship --display-name="Python (ML Internship)"
```

---

## 🚀 Execution Guide

1. Launch VS Code in the root directory:
   ```bash
   code .
   ```
2. Open any `.ipynb` file from the respective module subdirectories.
3. Select the registered kernel from the top-right kernel picker: **`Python (ML Internship)`**.
4. Run all cells sequentially to verify outputs and visualizations.

---

## 📝 Submission & Deliverables

- **Task-1 Detailed Report:** Located at `report/Task-1-Data-Science-Fundamentals.docx`
- **Submission Requirements Fulfilled:**
  - Complete modular notebooks (`.ipynb`) with markdown notes and code outputs.
  - End-to-end practical linear regression assignment.
  - Monorepo structure prepared for GitHub submission.
  - Comprehensive report and portal description (>200 words).

---

## 👤 Author & Acknowledgments

* **Intern / Author:** Durgesh Maurya
* **Role:** Machine Learning Engineer Intern
* **Organization:** YuvaIntern
* **Track:** 8-Week Machine Learning Engineer Internship
* **GitHub:** [@your-github-username](https://github.com/durgesh693)
* **LinkedIn:** [Durgesh Maurya](https://linkedin.com/in/durgesh277208)