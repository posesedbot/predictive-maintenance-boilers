from fastapi import FastAPI 
from pydantic import BaseModel 
 
app = FastAPI(title="Predictive Maintenance API") 
 
from pydantic import BaseModel, Field 

class SensorReadings(BaseModel): 
  run_hours: float = Field(ge=0, le=50000) 
  temp_avg: float = Field(ge=-50, le=300) 
  pressure_avg: float = Field(ge=0, le=100) 
  vibration: float = Field(ge=0, le=50) 
def heuristic_predict(run_hours: float, vibration: float) -> int: 
    return int((run_hours >= 1500) and (vibration > 2.0)) 
 
@app.post("/predict") 
def predict_failure(readings: SensorReadings): 
    y_pred = heuristic_predict(readings.run_hours, readings.vibration) 
    action = ( 
        "IMMEDIATE SHUTDOWN & INSPECTION. Failure triggered by high Run Hours (>1500 hrs) and high Vibration (>2.0)." 
        if y_pred == 1 
        else "No immediate action required. Continue routine monitoring." 
    ) 
    # ... (Lines where you apply the heuristic rule and define the 'action' string)

    # Note: 'y_pred' and 'action' must be defined above this line.

    return { 
        "prediction": y_pred, 
        "action_required": action, 
        "inputs": readings.dict() 
    } 
# Nothing else goes inside the predict_failure function after this line!

Local smoke test (run these after uvicorn api.fastapi_app:app --reload):

curl -s -X POST "http://127.0.0.1:8000/predict" \ 
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