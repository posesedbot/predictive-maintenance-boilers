# Predictive Maintenance for Industrial Boilers

## Project Status
[![CI Workflow Status](https://github.com/posesedbot/predictive-maintenance-boilers/actions/workflows/ci.yml/badge.svg)](https://github.com/posesedbot/predictive-maintenance-boilers/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🏗️ Domain-Driven Engineering
This project bridges the gap between mechanical reliability and predictive analytics. Drawing from professional experience in boiler maintenance and fabrication, this model focuses on the physical variables—Temperature, Pressure, and Vibration—that dictate industrial uptime.

## 🚀 Key Features
* **Production-Ready API:** Built with **FastAPI**, designed for low-latency integration with SCADA systems or maintenance dashboards.
* **Automated Quality Gates:** Integrated **GitHub Actions** CI/CD pipeline that enforces strict metric thresholds (Recall ≥ 0.95) before any code is merged.
* **Explainable Logic:** Includes both heuristic-based baselines and ML models to ensure predictions are interpretable by site engineers.

## 📊 Performance & Findings
The model was evaluated using a stratified holdout strategy. All baseline models achieved robust performance, validating the signal in the sensor data.

| Metric | Threshold (CI Gate) | Current Result |
| :--- | :--- | :--- |
| **Accuracy** | 0.90 | **1.00** |
| **Precision** | 0.90 | **1.00** |
| **Recall** | 0.95 | **1.00** |

> **Note on Performance:** The perfect scores reflect the robust signal in the current dataset. The pipeline is architected to be "failure-safe," prioritizing **Recall** to ensure no potential boiler failure goes undetected.

---

## 🛠️ How to Run

### 1. Setup
Create a virtual environment and install the required external libraries:
```bash
pip install -r requirements.txt
