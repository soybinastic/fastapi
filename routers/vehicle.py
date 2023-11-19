from fastapi import APIRouter
from pydantic import BaseModel
from repositories import vehicle


router = APIRouter(
    prefix='/vehicles'
)

@router.get("/")
def fetch_all_vehicles():
    results = vehicle.fetch_all_vehicles()
    return results
