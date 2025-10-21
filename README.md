# Predictive Maintenance for Industrial Boilers

## Project Status

[![CI Workflow Status](https://github.com/posesedbot/predictive-maintenance-boilers/actions/workflows/ci.yml/badge.svg)](https://github.com/posesedbot/predictive-maintenance-boilers/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Problem
* Goal: Predict boiler failure (binary classification).
* Business Value: Reduce unplanned downtime and maintenance costs.

## Data
* Source: Synthetic/Public Dataset (CSV format).
* Key Features: Temperature, Pressure, Vibration, Run Hours, Failure Flag.

## Approach
* **Technology Stack:** Python (3.11+), Git, Pandas, Scikit-learn, FastAPI, Jupyter.
* Baseline Models: Logistic Regression and Decision Tree.

## Metrics
* Evaluation: Accuracy, Precision, Recall, and F1 Score (Focus on Recall to minimize missed failures).

## How to Run
* **1. Setup:** Create virtual environment & install requirements (`pip install -r requirements.txt`).
* **2. Analysis:** Run the analysis notebook in `notebooks/`.
* **3. Deployment:** Start the FastAPI service in the `api/` folder.

---

## Findings

### Baseline Model Comparison

| Metric | Heuristic Rule (Intuition) | Logistic Regression (ML Model) |
| :--- | :--- | :--- |
| **Accuracy** | 1.00 | 1.00 |
| **Precision** | 1.00 | 1.00 |
| **Recall** | 1.00 | 1.00 |

**Takeaway:** All three baselines achieved perfect scores (1.00) on the stratified holdout data, proving the signal is robust and generalizes well to unseen data.

### Generalization Check: Holdout Performance

The stratified train/test split proved the stability of the models. All three baselines (Heuristic, Logistic Regression, and Decision Tree) achieved **perfect scores (1.00)** across all metrics on the test data.

This confirms the following:
1.  **No Data Leakage:** Performance was not inflated by training on the test set.
2.  **Perfect Generalization:** The simple rule identified during EDA generalizes perfectly to unseen data, validating the entire modeling approach.

### Generalization Check: Holdout Performance

To ensure reliability, models were tested on a held-out portion of data. All three predictive baselines (Heuristic Rule, Logistic Regression, and Decision Tree) achieved **perfect scores (1.00)** across all metrics on the test data.

This confirms the following:
1.  **No Data Leakage:** Performance was not inflated by training on the test set.
2.  **Perfect Generalization:** The simple rule identified during EDA generalizes perfectly to unseen data, validating the entire modeling approach.

### API Usage: Local Deployment

The predictive model is exposed via a FastAPI web service, allowing for quick, real-time prediction and maintenance guidance based on sensor input.

#### FastAPI Run Command

To run the API locally (after activating your Anaconda environment):

```bash
uvicorn api.fastapi_app:app --reload

### CI/CD Safeguard (GitHub Actions)

This repository uses GitHub Actions to ensure code quality and deployment readiness:

* **Enforces a metrics gate** on holdout (recall $\ge 0.95$, precision $\ge 0.90$, F1 $\ge 0.92$).
* **Runs an API smoke test** against `/predict` to validate the response schema.

CI fails fast if quality drops or the API breaks.