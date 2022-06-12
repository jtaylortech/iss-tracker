import requests
from datetime import datetime

my_lat = 32.613003
my_lng = -83.624199

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour) # I needed the current hour to be displayed so I can know how far I am off from the sunrise and sunset