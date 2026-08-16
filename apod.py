import os
from dotenv import load_dotenv

import requests

load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")

url = "https://api.nasa.gov/planetary/apod"

date_input = input("Enter a date (YYYY-MM-DD) or press Enter for today: ").strip()

params = {"api_key": API_KEY}
if date_input:
    params["date"] = date_input

response = requests.get(url, params=params)
data = response.json()
print("Status code:", response.status_code)
print("Full response:", data)

if response.status_code != 200:
    print("Error:", data.get("msg", "Something went wrong. Check your date format (YYYY-MM-DD)."))
else:
    print("Title:", data["title"])
    print("Date:", data["date"])
    print("Explanation:", data["explanation"])
    print("Image URL:", data.get("url"))