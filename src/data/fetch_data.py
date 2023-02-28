import json
import requests
import os

# kje si bomo shranili raw podatke
filename = "data/raw/data.json" 
# ustvarimo folder in datoteko ce se ne obstaja
os.makedirs(os.path.dirname(filename), exist_ok=True)

# naredimo request
file = requests.get('https://arsoxmlwrapper.app.grega.xyz/api/air/archive')
# pridobimo json podatke
podatki = file.json()

# zapisemo podatke v datoteko
with open(filename, 'w') as f:
    json.dump(podatki, f)

