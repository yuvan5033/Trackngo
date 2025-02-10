import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

class Transmitter:
    def __init__(self):
        if not SUPABASE_URL or not SUPABASE_API_KEY:
            raise ValueError("Supabase URL or API key is missing.")
        self.supabase_url = f"{SUPABASE_URL}/rest/v1"
        self.headers = {
            "apikey": SUPABASE_API_KEY,
            "Authorization": f"Bearer {SUPABASE_API_KEY}",
            "Content-Type": "application/json"
        }

    def send_data(self, table_name: str, bus_id: str, lat: float, long: float, headcount: int) -> bool:
        latitude = round(lat, 6)
        longitude = round(long, 6)
        payload = {
            "bus_id": bus_id,
            "latitude": latitude,
            "longitude": longitude,
            "headcount": headcount
        }
        url = f"{self.supabase_url}/{table_name}"
        response = requests.post(url, headers=self.headers, json=payload)

        if response.status_code == 201:
            print(f"Data successfully transmitted: {payload}")
            return True
        else:
            print(f"Error transmitting data: {response.status_code}, {response.text}")
            return False