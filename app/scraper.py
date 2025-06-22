import requests
from bs4 import BeautifulSoup

def fetch_flight_info(code, number, date):
    url = f"https://www.flightstats.com/v2/flight-tracker/{code}/{number}?year={date[:4]}&month={int(date[5:7])}&date={int(date[8:])}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    # Dummy parsing logic
    info = {
        "airline": code,
        "flight_number": number,
        "departure_date": date,
        "status": "On Time"  # You can update this based on parsed DOM
    }
    return info
