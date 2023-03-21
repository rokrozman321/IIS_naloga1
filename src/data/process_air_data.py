import json
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import os
import pandas as pd
import time
from datetime import datetime

import fnmatch


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

process_weather_data()