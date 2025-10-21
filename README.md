# Predictive Maintenance for Industrial Boilers

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

## Next Steps (Week 1)

* Train/test split check for leakage and holdout metrics
* Minimal FastAPI /predict stub deployed locally, returning prediction + heuristic-based maintenance action
* Short LinkedIn TL;DR post announcing baseline results (1–2 lines + repo link)