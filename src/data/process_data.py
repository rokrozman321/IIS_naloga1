import pandas as pd
import json


filename = "data/raw/data.json"
data_dict = pd.read_json(filename)

d = []

print(data_dict)
for i in range(len(data_dict)):
    temp=data_dict['json'][i]
    json_object = json.loads(temp)
    if i == 0:
        print(json_object['arsopodatki']['postaja'][14]['no2'])
        if(json_object['arsopodatki']['postaja'][14]['no2'] == ''):
            print('ok')
        else:
            print('ne')
        print(type(json_object['arsopodatki']['postaja'][14]['no2']))

    # print(json_object['arsopodatki']['postaja'][14])

    d.append(
        {
            'no2': json_object['arsopodatki']['postaja'][14]['no2'] if not json_object['arsopodatki']['postaja'][14]['no2'] == '' else None,
            'pm2.5': json_object['arsopodatki']['postaja'][14]['pm2.5'] if not json_object['arsopodatki']['postaja'][14]['pm2.5'] == '' else None,
            'datum_od': json_object['arsopodatki']['postaja'][14]['datum_od'] if not json_object['arsopodatki']['postaja'][14]['datum_od'] == '' else None,
            'o3': json_object['arsopodatki']['postaja'][14]['o3'] if not json_object['arsopodatki']['postaja'][14]['o3'] == '' else None,
            'pm10': json_object['arsopodatki']['postaja'][14]['pm10'] if not json_object['arsopodatki']['postaja'][14]['pm10'] == '' else None,
            'datum_do': json_object['arsopodatki']['postaja'][14]['datum_do'] if not json_object['arsopodatki']['postaja'][14]['datum_do'] == '' else None
        })

df = pd.DataFrame(d)
print(df)

# missing data
print(df.isnull().sum())
