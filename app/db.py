from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Flight

engine = create_engine("sqlite:///flights.db")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def save_to_db(data):
    session = Session()
    flight = Flight(**data)
    session.add(flight)
    session.commit()
    session.close()
