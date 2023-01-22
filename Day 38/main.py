import requests
from datetime import datetime
import os

# --------------------------------- Defined passwords and id in environment ----------------

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
API_USERNAME = os.environ["API_USERNAME"]
API_PASSWORD = os.environ["API_PASSWORD"]

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}

# --------------------------------- Extracting data from nutritionix  ----------------------

Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 59
HEIGHT_CM = 174
AGE = 17

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(Endpoint, json=parameters, headers=headers)
result = response.json()

# --------------------------------- Uploading data in google sheete ----------------

google_sheet_url = "https://api.sheety.co/34631ec83d7e0fb140930af1051a3fc1/myWorkout/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for items in range(len(result["exercises"])):
    activity = result['exercises'][items]["user_input"]
    duration = result['exercises'][items]["duration_min"]
    calories = result['exercises'][items]["nf_calories"]
    print(activity,duration,calories)

    values = {
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":activity,
            "duration":duration,
            "calories":calories
        }
    }

    sheet_response = requests.post(google_sheet_url,json=values,auth=(API_USERNAME,API_PASSWORD,))
    print(sheet_response.text)

# --------------------------------- The End ----------------------------------------------------