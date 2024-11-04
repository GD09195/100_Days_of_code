import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 19.432057 # Your latitude
MY_LONG = -99.094975 # Your longitude

source_mail = 'gdtest0912@gmail.com'
source_password = 'uantymuzhufwozwy'

def send_mail()->None:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=source_mail, password=source_password)
        connection.sendmail(
            from_addr=source_mail,
            to_addrs=source_mail,
            msg="Subject: Look up!\n\nThe ISS is above you in the sky!"
        )

def utc_to_cst(time_utc)->int:
    diff = 6
    if time_utc-diff < 0:
        return 24-(diff-time_utc)
    else:
        return time_utc-diff

def under_iss_range()->bool:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    latitude_difference = MY_LAT - iss_latitude
    longitude_difference = MY_LONG - iss_longitude

    #print(f'({MY_LAT}, {MY_LONG})')
    #print(f'({iss_latitude},{iss_longitude})')
    #print(latitude_difference)
    #print(longitude_difference)

    # Your position is within +5 or -5 degrees of the ISS position.
    return abs(longitude_difference) <= 5 and abs(latitude_difference) <=5

def is_night()->bool:

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()
    sunrise_hour = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    #Converting to CST
    sunset_hour = utc_to_cst(sunset_hour)
    sunrise_hour = utc_to_cst(sunrise_hour)

    return not sunset_hour > time_now.hour > sunrise_hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

while True:
    time.sleep(60)
    if under_iss_range() and is_night():
        send_mail()
# BONUS: run the code every 60 seconds.



