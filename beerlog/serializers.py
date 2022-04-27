from pydantic import BaseModel, validator
from datetime import datetime
from fastapi import HTTPException, status


class BeerOut(BaseModel):
    id: int
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int
    date: datetime


class BeerIn(BaseModel):
    name: str
    style: str
    flavor: int
    image: int
    cost: int

    @validator("image", "flavor", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v
