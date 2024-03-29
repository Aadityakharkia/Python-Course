import requests
from datetime import datetime
import smtplib
import time

#-------------------------------------------------------- Defining passwords and username ----------------------------------

MY_EMAIL = "Your_Mail_ID"
MY_PASSWORD = "Your_Password"
MY_LAT = 30.316496
MY_LONG = 78.032188

#------------------------------------------------------ Locating ISS location ----------------------------------------------

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

#------------------------------------------------------ Comparing ISS location with my location ----------------------------

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#------------------------------------------------------ Sending the Email ---------------------------------------------------


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="Your Mail",
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )

#------------------------------------------------------- Future Work -------------------------------------------------------

# Sending SMS
# Making it more accurate
# Searching different location
