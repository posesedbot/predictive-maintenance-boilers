# api/fastapi_app.py

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

# --- 1. Define the Input Data Structure (Pydantic Model) ---
# This ensures incoming data is correct
class SensorReadings(BaseModel):
    run_hours: float
    temp_avg: float
    pressure_avg: float
    vibration: float

# --- 2. Initialize the FastAPI App ---
app = FastAPI(title="Boiler Predictive Maintenance API")

# NOTE: For a simple, perfect heuristic, we don't need to load the Scikit-learn model,
# but we will simulate the prediction logic directly for speed and clarity.
# In a real project, we would save and load the trained DT model here.

# --- 3. The /predict Endpoint ---
@app.post("/predict")
def predict_failure(readings: SensorReadings):
    """
    Accepts sensor readings and predicts boiler failure based on the heuristic rule.
    """
    
    # Extract key values for the human-readable rule
    run_hours = readings.run_hours
    vibration = readings.vibration

    # Apply the Heuristic Rule: Failure if Run Hours >= 1500 AND Vibration > 2.0
    if run_hours >= 1500 and vibration > 2.0:
        prediction = 1
        maintenance_action = "IMMEDIATE SHUTDOWN & INSPECTION. Failure triggered by high Run Hours (>1500 hrs) and high Vibration (>2.0)."
    else:
        prediction = 0
        maintenance_action = "STATUS OK. Below critical failure thresholds."

    return {
        "prediction": prediction,
        "action_required": maintenance_action,
        "run_hours_input": run_hours,
        "vibration_input": vibration
    }

# --- 4. OPTIONAL: Root Endpoint ---
@app.get("/")
def read_root():
    return {"status": "Boiler Maintenance API is running."}

# To run this app:
# 1. Ensure you have activated your environment (source venv/Scripts/activate or Anaconda Prompt)
# 2. Run: uvicorn api.fastapi_app:app --reload