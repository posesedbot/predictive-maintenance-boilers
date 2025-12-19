"""
FastAPI application exposing a simple heuristic model for predictive maintenance.

The API defines a root endpoint for health checking and a `/predict` endpoint that
accepts sensor readings and returns a prediction along with a recommended action.

The heuristic is intentionally simple: if the run hours exceed 1500 and the
vibration exceeds 2.0 units, the model predicts imminent failure. In that
scenario, the API recommends an immediate shutdown and inspection. Otherwise it
returns a `STATUS OK` message indicating normal operation.

This module is designed to be minimal and self-contained so that it can be
deployed via `uvicorn api.fastapi_app:app` without bringing in any external
dependencies beyond FastAPI and Pydantic (which are specified in
requirements.txt).
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Predictive Maintenance API")


class SensorReadings(BaseModel):
    """Input schema for sensor readings.

    Validates that inputs fall within reasonable engineering ranges to catch
    out-of-bound values early. All fields are required.
    """

    run_hours: float = Field(..., ge=0, le=50_000, description="Cumulative run time in hours")
    temp_avg: float = Field(..., ge=-50, le=300, description="Average operating temperature")
    pressure_avg: float = Field(..., ge=0, le=100, description="Average operating pressure")
    vibration: float = Field(..., ge=0, le=50, description="Average vibration level")


def heuristic_predict(run_hours: float, vibration: float) -> int:
    """Apply a simple rule to determine if maintenance is required.

    Args:
        run_hours: Total accumulated operating hours for the boiler.
        vibration: Average measured vibration level.

    Returns:
        1 if the run hours exceed 1500 *and* vibration exceeds 2.0, otherwise 0.
    """
    return int((run_hours >= 1500) and (vibration > 2.0))


@app.get("/")
def read_root() -> dict[str, str]:
    """Health‑check endpoint returning a simple status message."""
    return {"status": "Boiler Maintenance API is running."}


@app.post("/predict")
def predict_failure(readings: SensorReadings) -> dict[str, object]:
    """Predict whether a boiler needs maintenance based on sensor input.

    Args:
        readings: A validated SensorReadings instance containing run hours,
            average temperature, average pressure and vibration level.

    Returns:
        A dictionary with a prediction flag (0 or 1), a human readable action
        recommendation, and echoes of the inputs for reference.
    """
    # Generate a binary prediction using the heuristic rule
    y_pred = heuristic_predict(readings.run_hours, readings.vibration)

    # Craft the action recommendation to satisfy smoke tests. The success case
    # must include the phrase "STATUS OK" while the failure case should
    # include "SHUTDOWN & INSPECTION".
    if y_pred == 1:
        action = (
            "IMMEDIATE SHUTDOWN & INSPECTION. Failure triggered by high Run Hours (>1500 hrs) "
            "and high Vibration (>2.0)."
        )
    else:
        # In the non‑failure case include the phrase "STATUS OK" followed by a descriptive
        # message. A colon after the status improves readability and satisfies smoke tests.
        action = "STATUS OK: No immediate action required. Continue routine monitoring."

    return {
        "prediction": y_pred,
        "action_required": action,
        "inputs": readings.dict(),
 }curl -s -X POST "http://127.0.0.1:8000/predict" \ 
  -H "Content-Type: application/json" \ 
  -d '{"run_hours":2000,"temp_avg":95.0,"pressure_avg":6.5,"vibration":2.8}' 
Expected shape:

{ 
  "prediction": 1, 
  "action_required": "IMMEDIATE SHUTDOWN & INSPECTION. Failure triggered by high Run Hours (>1500 hrs) and high Vibration (>2.0).", 
  "run_hours_input": 2000.0, 
  "vibration_input": 2.8, 
  "temp_avg_input": 95.0, 
  "pressure_avg_input": 6.5 
} 
