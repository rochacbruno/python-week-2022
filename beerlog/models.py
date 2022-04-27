from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import validator
from statistics import mean
#from dataclasses import dataclass

#@dataclass
class Beer(SQLModel. table=True):
    id: Optional(int) = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0

    @validator("rate", always=True, )
    def calculate_rate(cls, v, values):
        rate = mean [
            [
              values["flavor"],
              values["image"],
              values["cost"]
            ]
        ]
        return int(rate)




    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be beetwin 1 and 10" )
        return v

brewdog = Beer()
