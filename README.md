# Ecommerce Product Delivery Prediction

[![CI](https://github.com/asirjeril/Ecommerce_Product_Delivery_Prediction/actions/workflows/ci.yml/badge.svg)](https://github.com/asirjeril/Ecommerce_Product_Delivery_Prediction/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/asirjeril/Ecommerce_Product_Delivery_Prediction/blob/main/notebooks/Ecommerce_Product_Delivery_Prediction.ipynb)

**Capstone project** to predict whether an e-commerce order is delivered on time using product, logistics, and customer features. Includes SHAP explainability and decision-threshold tuning.

---

## ✨ Objective
Build a robust ML pipeline that:
- Predicts on-time vs. late delivery.
- Explains key drivers with **SHAP**.
- Tunes the **probability threshold** to balance precision/recall for the “late” class.

## 🗂️ Repository Structure
```
.
├── .github/workflows/ci.yml               # Lint + tests on every push/PR
├── data/
│   ├── Ecommerce_Product_Delivery_Prediction.csv (optional; use LFS if large)
│   └── sample.csv                         # tiny sample for CI
├── docs/
│   ├── Ecommerce_Product_Delivery_Prediction_Description.docx
│   └── model_card.md
├── notebooks/
│   └── Ecommerce_Product_Delivery_Prediction.ipynb
├── reports/
│   └── figures/
│       ├── shap_summary_bar.png
│       ├── shap_summary_beeswarm.png
│       ├── threshold_tuning.png
│       ├── model_comparison_f1.png
│       └── <confusion_matrices>.png
├── src/ecommerce_delivery/
│   ├── __init__.py
│   └── train_and_evaluate.py              # CLI: train/eval/SHAP/threshold
├── tests/
│   └── test_smoke.py
├── .gitignore
├── environment.yml
├── requirements.txt
├── LICENSE
└── README.md
```

## 📦 Environment
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Quickstart (CLI)
```bash
python -m src.ecommerce_delivery.train_and_evaluate   --data data/Ecommerce_Product_Delivery_Prediction.csv   --out reports/figures   --do_shap --do_threshold
```
Artifacts saved to `reports/figures/`:
- `shap_summary_bar.png`, `shap_summary_beeswarm.png`
- `threshold_tuning.png`, `threshold_metrics.csv`, `best_threshold.json`
- `model_comparison_f1.png`, confusion matrices, `metrics.json`

## 📓 Notebook
Open the end-to-end workflow in the notebook:
- `notebooks/Ecommerce_Product_Delivery_Prediction.ipynb`
(Use the **Open in Colab** badge above if you prefer the cloud.)

## 🧠 Methods
- **EDA:** distributions, correlations, categorical vs. target analysis  
- **Preprocessing:** label encoding for categoricals, stratified split  
- **Models:** Decision Tree, Random Forest, Logistic Regression, KNN  
- **Evaluation:** Accuracy, Precision, Recall, F1, confusion matrices  
- **Explainability:** Global SHAP (bar + beeswarm)  
- **Operations:** Threshold sweep to optimize business metric (F1 or recall for late deliveries)

## 📊 Dataset (columns)
See `docs/Ecommerce_Product_Delivery_Prediction_Description.docx`.  
**Target:** `Reached.on.Time_Y.N` (1 = NOT on time, 0 = on time).

## 🔎 Results (example)
DT / RF typically ~0.65–0.70 accuracy on hold-out; use **F1** for the late class.  
Threshold tuning enables trading precision vs recall depending on ops needs.

## 🧭 Roadmap
- Class-weighted models & calibrated probabilities  
- SHAP dependence/interaction plots  
- MLflow experiment tracking, DVC data versioning  
- GitHub Pages mini-report (auto-renders figures)

## 🤝 Contributing
PRs welcome! Run `black`, `flake8`, and `pytest` before opening a PR.

## 📄 License
MIT © 2025 asirjeril
