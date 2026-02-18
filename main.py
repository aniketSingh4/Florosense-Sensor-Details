from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://localhost:3001"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# url end point along with api-key
CLOUD_BASE_URL = "https://api.florosense.cloud/api/v1/dashboard/sensors"

API_KEY = "x9pkeaSq5Kk96KknSweTS3EnUIuFvCnZ"


@app.get("/sensor-data/{sensor_id}")
def get_sensor_data(sensor_id: str):
    try:
        cloud_url = f"{CLOUD_BASE_URL}/{sensor_id}/latest"

        headers = {
            "x-api-key": API_KEY
        }


        response = requests.get(cloud_url, headers=headers, timeout=10)

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )

        try:
            return response.json()
        except:
            raise HTTPException(
                status_code=500,
                detail="Invalid JSON from cloud"
            )

    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail="Cloud connection failed"
        )

# @app.get("/sensor-data/{sensor_id}")
# def get_sensor_data(sensor_id: str):
#     try:
#         cloud_url = f"{CLOUD_BASE_URL}/{sensor_id}/latest"

#         headers = {
#             "x-api-key": API_KEY
#         }

#         response = requests.get(cloud_url, headers=headers, timeout=10)

#         print("Cloud Status:", response.status_code)
#         print("Cloud Response:", response.text)

#         if response.status_code != 200:
#             raise HTTPException(
#                 status_code=response.status_code,
#                 detail=response.text
#             )

#         return response.json()

#     except Exception as e:
#         print("Backend Error:", str(e))
#         raise HTTPException(status_code=500, detail=str(e))


# @app.get("/sensor-data/{sensor_id}")
# def get_sensor_data(sensor_id: str):
#     return {
#         "sensor_id": sensor_id,
#         "timestamp": "2026-02-16T10:30:00",
#         "pm25": 25,
#         "pm10": 40,
#         "temperature": 30,
#         "humidity": 60
#     }
