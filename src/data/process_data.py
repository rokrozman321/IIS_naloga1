import json
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import os
import pandas as pd
import time
from datetime import datetime

import fnmatch

def convert_datetime(dt_str):
    dt_obj = datetime.strptime(dt_str, '%Y-%m-%d %H:%M')
    return datetime.strftime(dt_obj, '%Y-%m-%d-%H:%M:%S')


def process_data():
    print("Process arso data")
    filename = "data/raw/data.json"
    data_dict = pd.read_json(filename)

    d = []

    for i in range(len(data_dict)):
        temp=data_dict['json'][i]
        json_object = json.loads(temp)

        d.append(
            {
                'no2': json_object['arsopodatki']['postaja'][14]['no2'] if not json_object['arsopodatki']['postaja'][14]['no2'] == '' \
                    and not json_object['arsopodatki']['postaja'][14]['no2'] == '<2' else np.nan,
                'pm2.5': json_object['arsopodatki']['postaja'][14]['pm2.5'] if not json_object['arsopodatki']['postaja'][14]['pm2.5'] == '' \
                    and not json_object['arsopodatki']['postaja'][14]['pm2.5'] == '<2' else np.nan,
                'datum_od': json_object['arsopodatki']['postaja'][14]['datum_od'] if not json_object['arsopodatki']['postaja'][14]['datum_od'] == '' else np.nan,
                'o3': json_object['arsopodatki']['postaja'][14]['o3'] if not json_object['arsopodatki']['postaja'][14]['o3'] == '' \
                    and not json_object['arsopodatki']['postaja'][14]['o3'] == '<2' else np.nan,
                'pm10': json_object['arsopodatki']['postaja'][14]['pm10'] if not json_object['arsopodatki']['postaja'][14]['pm10'] == '' \
                    and not json_object['arsopodatki']['postaja'][14]['pm10'] == '<2' else np.nan,
                'datum_do': json_object['arsopodatki']['postaja'][14]['datum_do'] if not json_object['arsopodatki']['postaja'][14]['datum_do'] == '' else np.nan
            })

    df = pd.DataFrame(d)

    # sort
    df.sort_values(by='datum_od', inplace=True)


    df['datetime'] = df['datum_od'].apply(convert_datetime)
    print(df)

    # drop datum_od in datum_do
    df = df.drop(['datum_od'], axis=1)
    df = df.drop(['datum_do'], axis=1)
    df.drop_duplicates(subset=['datetime'], inplace=True)
    print(df)   

    # fill missing data
    # povp
    print(df.isnull().sum())
    # df.fillna(df.mean())
    df['no2'].fillna((df['no2'].mean()), inplace=True)
    df['pm2.5'].fillna((df['pm2.5'].mean()), inplace=True)
    df['o3'].fillna((df['o3'].mean()), inplace=True)
    df['pm10'].fillna((df['pm10'].mean()), inplace=True)
    print(df.isnull().sum())

    print(df)    
    
    # kje si bomo shranili raw podatke
    filename = "data/processed/arso_data.csv" 

    # ustvarimo folder in datoteko ce se ne obstaja
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    df.to_csv(filename, index=False)

def process_weather_data():
    print("Process weather data")
    data = json.load(open('data/raw/weather/air_data.json'))
    df = pd.DataFrame(data['days'])
    # print(df['datetime'])
    df_hours = df['hours']
    # print(df_hours[6][23]['datetime'])
    # print(df_hours[6][23]['temp'])

    # zdruzimo datum in cas 
    date = str(df['datetime'][7]) 
    # print(date)
    temps = []
    datetimes = []

    for i in range(0,8):
        for j in range(0,24):
            # if j<10:
                date1 = df['datetime'][i]
                time1 = df_hours[i][j]['datetime']
                temp1 = df_hours[i][j]['temp']
                datetime_v = date1 + '-' + time1
                datetimes.append(datetime_v)
                temps.append(temp1)

    # print(datetimes)
    # print(temps)
    
    # preverimo ce se ujema
    # print(datetimes[1])
    # print(temps[1])

    # print(df['datetime'][0])
    # print(df_hours[0][1]['datetime'])
    # print(df_hours[0][1]['temp'])

    df2 = pd.DataFrame()
    df2['datetime'] = datetimes
    df2['temps'] = temps

    print(df2)
    
    # kje si bomo shranili raw podatke
    filename = "data/processed/air_data.csv" 

    # ustvarimo folder in datoteko ce se ne obstaja
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    df2.to_csv(filename, index=False)

def merge_data():
    print("Merge data")
    file1 = "data/processed/air_data.csv" 
    file2 = "data/processed/arso_data.csv" 

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # print(df1)
    # print(df2)

    df_l = pd.merge(df1, df2, on="datetime", how="left")

    # print(df_l.isnull().sum())

    print(df_l)

    # kje si bomo shranili raw podatke
    filename = "data/processed/merged.csv" 

    # ustvarimo folder in datoteko ce se ne obstaja
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    df_l.to_csv(filename, index=False)
