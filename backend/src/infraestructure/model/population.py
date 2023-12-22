from pydantic import BaseModel, Field

class Population(BaseModel):
    country: str = Field(...)
    populationCount: int  = Field(...)
    areaKiloMeters: int  = Field(...)
    createdAt:str = Field(...)
    
    class Config:
        populate_by_name = True
        schema_extra = {
            "example": {
                "country": "Non Where",
                "populationCount": 1,
                "areaKiloMeters": 1
            }
        }
