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

process_data()