import pandas as pd
import json


filename = "data/raw/data.json"
data_dict = pd.read_json(filename)

d = []

print(data_dict)
for i in range(len(data_dict)):
    temp=data_dict['json'][i]
    json_object = json.loads(temp)
    # print(json_object['arsopodatki']['postaja'][14])
    d.append(
        {
            'no2': json_object['arsopodatki']['postaja'][14]['no2'],
            'pm2.5': json_object['arsopodatki']['postaja'][14]['pm2.5'],
            'datum_od': json_object['arsopodatki']['postaja'][14]['datum_od'],
            'o3': json_object['arsopodatki']['postaja'][14]['o3'],
            'pm10': json_object['arsopodatki']['postaja'][14]['pm10'],
            'datum_do': json_object['arsopodatki']['postaja'][14]['datum_do']
        })

df = pd.DataFrame(d)
print(df)
