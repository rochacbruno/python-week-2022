from typing import Optional
from fastapi import FastAPI
from beerlog.core import get_beers_from_database

api = FastAPI(title="beerlog")


@api.get("/beers/")
def list_beers(style: Optional[str] = None):
    """Lists beers from the database"""
    beers = get_beers_from_database(style)
    return beers
