from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True)
    airline = Column(String)
    flight_number = Column(String)
    departure_date = Column(String)
    status = Column(String)
