# FlightStats Scraper API

## Setup

```bash
git clone <your-repo-url>
cd flight_api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Endpoint

```http
GET /flights?airline_code=AI&airline_number=101&departure_date=2024-06-20
```

## Testing

```bash
pytest
```
