"""
FastAPI application exposing a simple heuristic model for predictive maintenance.
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
    """Apply a simple rule to determine if maintenance is required."""
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
        # Updated from .dict() to .model_dump() for Pydantic V2 compliance
        "inputs": readings.model_dump(),
    }
