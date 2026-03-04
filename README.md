# 🛍️ Shopping Trends Analysis

> In-depth Exploratory Data Analysis (EDA) on customer shopping behaviors to uncover purchasing patterns and drive strategic sales decisions.

---

## 📌 Project Overview

This project performs a structured EDA on a large dataset of customer shopping behaviors. The data was processed and cleaned to identify purchasing patterns, improving the reliability of sales strategy insights for business stakeholders.

---

## ❗ Problem Statement

Raw sales data contains noise and lacks structure, making it hard to derive strategic insights. Without proper cleaning and analysis, businesses risk making decisions based on incomplete or misleading information.

---

## 🔍 What I Built

A structured EDA pipeline using Python libraries to:
- Clean and preprocess raw shopping data
- Visualize hidden trends in consumer behavior
- Surface actionable business recommendations

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Core programming language |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | Data manipulation & cleaning |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat) | Data visualization |
| Seaborn | Statistical plots |
| Jupyter Notebook | Interactive analysis environment |

---

## 📁 Repository Structure

```
shopping-trends-analysis/
│
├── data/
│   └── shopping_trends.csv        # Raw dataset (place here)
│
├── notebooks/
│   └── shopping_trends_eda.ipynb  # Main analysis notebook
│
├── src/
│   ├── data_loader.py             # Data loading utilities
│   ├── cleaner.py                 # Data cleaning functions
│   └── visualizer.py              # Reusable plot functions
│
├── outputs/
│   └── figures/                   # Saved charts & plots
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Implementation Steps

1. **Data Loading** — Imported the customer shopping dataset into a Pandas DataFrame
2. **Data Profiling** — Inspected data types, missing values, and statistical summaries
3. **Data Cleaning** — Removed duplicates and imputed missing values for data quality
4. **Univariate Analysis** — Analyzed distribution of individual variables (Age, Purchase Amount, Category)
5. **Bivariate Analysis** — Explored relationships such as `Gender vs. Spending` and `Season vs. Sales`
6. **Pattern Recognition** — Identified peak shopping hours and top-selling product categories
7. **Insight Generation** — Summarized findings into actionable business recommendations

---

## 💡 Key Learnings & Impact

- ✅ **Processed Large Datasets** — Handled and optimized a high-volume customer dataset efficiently
- ✅ **Cleaned Data Pipeline** — Built a reusable cleaning pipeline reducing data noise significantly
- ✅ **Actionable Sales Insights** — Delivered findings that can directly inform sales and marketing strategy

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/shopping-trends-analysis.git
cd shopping-trends-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add the dataset
Place `shopping_trends.csv` in the `data/` folder.
> Dataset available on [Kaggle – Customer Shopping Trends Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset)

### 4. Launch the notebook
```bash
jupyter notebook notebooks/shopping_trends_eda.ipynb
```

---

## 📊 Sample Insights

- 📈 Peak purchasing seasons identified with clear sales spikes
- 👥 Gender-based spending differences uncovered across product categories  
- 🏷️ Top product categories ranked by revenue contribution
- ⏰ High-conversion time windows mapped for targeted campaigns

---

## 👤 Author

**Md Rayan**  
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-blue?style=flat)](https://md-rayan-portfolio.vercel.app)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
