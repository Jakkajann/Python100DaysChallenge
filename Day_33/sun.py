import requests
from datetime import datetime

MY_LAT = -25.094700
MY_LONG = -50.163158
SUNRISE_URL = "https://api.sunrise-sunset.org/json"

params = {
    "lat": MY_LAT,
    "lgn": MY_LONG,
    "formatted": int(0),
}

response = requests.get(url=SUNRISE_URL, params=params)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
now_hour = time_now.hour