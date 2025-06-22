from pydantic import BaseModel

class FlightResponse(BaseModel):
    airline: str
    flight_number: str
    departure_date: str
    status: str
