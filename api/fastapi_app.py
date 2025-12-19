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
def root():
    return {"status": "Boiler Maintenance API is running."}

@app.post("/predict")
def predict_failure(readings: SensorReadings) -> dict[str, object]:
    y_pred = heuristic_predict(
        readings.run_hours,
        readings.vibration,
    )

    if y_pred == 1:
        action = (
            "IMMEDIATE SHUTDOWN & INSPECTION. "
            "Failure triggered by high Run Hours (>1500 hrs) "
            "and high Vibration (>2.0)."
        )
    else:
        action = "STATUS OK: No immediate action required. Continue routine monitoring."

    return {
        "prediction": y_pred,
        "action_required": action,
        "inputs": readings.dict(),
    }
