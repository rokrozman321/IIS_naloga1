import json
import requests
import os
import time

def weather_data():
    print("Fetch air data")
    filename = "data/raw/weather/air_data.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/koper/last7days?unitGroup=metric&key=X4RTJCZPEDYGRTD942B5FXABP&contentType=json')
    # pridobimo json podatke
    podatki = file.json()

    # zapisemo podatke v datoteko
    with open(filename, 'w') as f:
        json.dump(podatki, f)

weather_data()