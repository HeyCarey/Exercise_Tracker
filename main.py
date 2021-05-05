import datetime
import requests
from requests.auth import HTTPBasicAuth



today_date = datetime.datetime.now().strftime("%m-%d-%Y")
today_time = datetime.datetime.now().strftime("%I:%M")
print(today_time)

# Nutritionix
APP_ID = "yourID"
APP_KEY = "yourKey"
GENDER = "yourGender"
AGE = "yourAge"

#Sheety
USER = "yourUsername"
PASS = "yourPassword"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/1927fcf604e160bff77566cd3f7fdf91/workoutTracking/workouts"

question = input("What exercise did you do? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
parameters = {
    "query": question,
    "gender": GENDER,
    "age": AGE,
    "weight_kg": 72.5748,
    "height_cm": 175.26
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# response.raise_for_status()

data = response.json()
exercise = data["exercises"][0]["user_input"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

########## SHEETY ##########

sheety_params = {
    "workout": {
        "date": today_date,
        "time": today_time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}
# bearer_headers = {
#     "Content-Type": "application/json",
#
# }
sheet_post = requests.post(sheety_endpoint, json=sheety_params, auth=HTTPBasicAuth(USER, PASS))

print(sheet_post.text)
