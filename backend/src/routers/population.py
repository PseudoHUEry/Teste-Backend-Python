from fastapi import APIRouter, Request
from typing import List
from ..infraestructure.model.population import Population
from ..application.insert_scrapped_data import insert_scrapped_data

router = APIRouter()

@router.get("/", response_description="List all population", response_model=List[Population])
def list_population(request: Request):
    populations = list(request.app.database["populations"].find(limit=100))
    return populations



@router.post("/generate", response_description="Exclude old information and collect the new one.", response_model=List[Population])
async def genetate_data(request: Request):
    result = await insert_scrapped_data()
    return result

