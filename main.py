import requests
from datetime import datetime
from credentials import *
import smtplib
import time

MY_EMAIL = jt_email
MY_PWORD = jt_pword
TO_EMAIL = alt_email

my_lat = 32.613003
my_lng = -83.624199


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # my position is within +- 5 degrees of the iss position
    if my_lat-5 <= iss_latitude <= my_lat+5 and my_lng-5 <= iss_longitude <= my_lng+5:
        return True


def is_night():
    parameters = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <=sunrise:
        return True
        # its dark

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addr=TO_EMAIL,
            msg="Subject:Look Up🛰👆🏽\n\nThe ISS is above you in the sky! Your program is working "
        )