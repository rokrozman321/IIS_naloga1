import json
import requests
import os
import time

def fetch_data():
    print("Fetch arso data")
    # kje si bomo shranili raw podatke
    filename = "data/raw/data.json" 

    # ustvarimo folder in datoteko ce se ne obstaja
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # naredimo request
    file = requests.get('https://arsoxmlwrapper.app.grega.xyz/api/air/archive')
    # pridobimo json podatke
    podatki = file.json()

    print("Shranjujemo v datoteko: " + filename)
    # zapisemo podatke v datoteko
    with open(filename, 'w') as f:
        json.dump(podatki, f)

fetch_data()