from fastapi import FastAPI, Query
from app.scraper import fetch_flight_info
from app.db import save_to_db
from app.schemas import FlightResponse

app = FastAPI()

@app.get("/flights", response_model=FlightResponse)
def get_flight_info(
    airline_code: str = Query(...),
    airline_number: str = Query(...),
    departure_date: str = Query(...)
):
    data = fetch_flight_info(airline_code, airline_number, departure_date)
    save_to_db(data)
    return data
