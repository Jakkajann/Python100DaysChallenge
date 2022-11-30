import requests
from datetime import datetime
import smtplib
import time

# Gmail doesn't accept smtp protocols from third app anymore

MY_LAT = -25.094700
MY_LONG = -50.163158
SUNRISE_URL = "https://api.sunrise-sunset.org/json"
ISS_URL = "http://api.open-notify.org/iss-now.json"
MY_EMAIL = "email@email.com"
MY_PASSWORD = "password"
TO_EMAIL = "fermocrosky@gmail.com"

params = {
    "lat": MY_LAT,
    "lgn": MY_LONG,
    "formatted": int(0),
}

def is_night():
    response = requests.get(url=SUNRISE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    now_hour = time_now.hour

    if now_hour >= sunset or time_now <= sunrise:
        return True

def is_iss_overhead():
    response = requests.get(url=ISS_URL)
    response.raise_for_status()

    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_compare = MY_LAT-5 <= iss_latitude <= MY_LAT+5
    long_compare = MY_LONG-5 <= iss_longitude <= MY_LONG+5

    if lat_compare and long_compare:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with (smtplib.SMTP("smtp.gmail.com")) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg="Subject:Look Up\n\nThe ISS is above you in the sky")
        print("send a email for me")