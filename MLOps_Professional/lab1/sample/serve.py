import uvicorn
import logging
import warnings

from fastapi import FastAPI, HTTPException
from data_model import MaintenancePayload
from maintenance import test_maintenance


appli = FastAPI()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore")


@appli.get("/ping")
async def ping():
    """Ping server to determine status

    Returns
    -------
    API response
        response from server on health status
    """
    return {"message":"Server is Running"}

@appli.post("/maintenance")
async def predict(payload:MaintenancePayload):
    
    maintenance_result = test_maintenance(payload.temperature, payload.hydraulic_pressure)
    return {"msg": "Completed Analysis", "Maintenance Status": maintenance_result}

@appli.post("/supportbot")
async def supportbot(request: dict):
    """Endpoint for supportbot

    Parameters
    ----------
    request : dict
        A request dictionary containing a 'text' key.

    Returns
    -------
    API response
        Hard-coded response for maintenance
    """
    if request.get("text") == "help":
        return {"response": "Bring the harvester in for maintenance"}
    else:
        raise HTTPException(status_code=400, detail="Invalid request") 

if __name__ == "__main__":
    uvicorn.run("serve:appli", host="0.0.0.0", port=5000, log_level="info")