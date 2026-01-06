import requests
from datetime import datetime as dt

header = {
'x-app-key' : "e3fddbfc4ec32bb005952f41669b1913",
'x-app-id' : "729fa61c"
}

params = {
    "query": input("What exercise did you do today?    "),
    "gender": "female",
    "weight_kg": 78,
    "height_cm": 168 ,
    "age": 18
    }


allexercise = requests.post(url = "https://trackapi.nutritionix.com/v2/natural/exercise", json = params, headers = header)
result = allexercise.json()
# json viewer not working for exercise.post()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

today_date = dt.now().strftime("%d/%m/%Y")
today_time = dt.now().strftime("%X")

for part in result["exercises"]:
    params2 = {
        "sheet1" : {
            "Date": today_date,
            "Time": today_time,
            "Exercise":part["name"].title(),
            "Duration":part["duration_min"],
            "Calories":part["nf_calories"]     }
    }

auth = {"Authorization": "Bearer 5c59u[ieqrhqe;ohqerqie;748g9m0v35cxp" }
response = requests.post(url = "https://api.sheety.co/92dc3544ea44615f832b03ce3d02a27d/workouts/sheet1", json = params2, headers = auth)
print(response.json())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
