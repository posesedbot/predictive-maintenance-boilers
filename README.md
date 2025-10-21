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

---

## Findings

### Baseline Model Comparison

| Metric | Heuristic Rule (Intuition) | Logistic Regression (ML Model) |
| :--- | :--- | :--- |
| **Accuracy** | 1.00 | 1.00 |
| **Precision** | 1.00 | 1.00 |
| **Recall** | 1.00 | 1.00 |

**Takeaway:** All three baselines achieved perfect scores (1.00) on the stratified holdout data, proving the signal is robust and generalizes well to unseen data.

### API Usage: Local Deployment

The predictive model is exposed via a FastAPI web service, allowing for quick, real-time prediction and maintenance guidance based on sensor input.

#### Run Server

To run the API locally (after activating your Anaconda environment):

```bash
uvicorn api.fastapi_app:app --reload