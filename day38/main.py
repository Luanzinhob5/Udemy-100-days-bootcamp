import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "180"
AGE = "18"

API_KEY_NUTRITIONIX = "3b17d6a01ab47521e47dd4b52bb483d7"
ID_NUTRITIONIX = "9ce829f5"

endpoint = "http://status.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/0daf027a30850361551eab8d0ccb15b9/workoutTracking/workouts"

exercise_text = input("Tell which exercise you did: ")

headers = {
    "x-app-id":ID_NUTRITIONIX,
    "x-app-key":API_KEY_NUTRITIONIX
}

parameters = {
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}


response = requests.post(url=endpoint,headers=headers,json=parameters)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

