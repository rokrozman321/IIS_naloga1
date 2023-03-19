import json
import requests
import os
import time

def fetch_data():
    # kje si bomo shranili raw podatke
    filename = "/Vaja1/data/raw/data1.json" 
    # filename = "/data/raw/data.json" 
    # ustvarimo folder in datoteko ce se ne obstaja
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # naredimo request
    file = requests.get('https://arsoxmlwrapper.app.grega.xyz/api/air/archive')
    # pridobimo json podatke
    podatki = file.json()

    # zapisemo podatke v datoteko
    with open(filename, 'w') as f:
        json.dump(podatki, f)

def weather_data():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    filename = "/Vaja1/data/raw/weather/" + timestr + ".json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/koper/last7days?unitGroup=metric&key=X4RTJCZPEDYGRTD942B5FXABP&contentType=json')
    # pridobimo json podatke
    podatki = file.json()

    # zapisemo podatke v datoteko
    with open(filename, 'w') as f:
        json.dump(podatki, f)

