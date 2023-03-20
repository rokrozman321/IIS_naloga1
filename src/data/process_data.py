import json
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import os
import pandas as pd
import time

import fnmatch

def process_data():
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

    # transform date
    df['datum_od'] = pd.to_datetime(df['datum_od'])
    df['leto_od'] = df['datum_od'].dt.year
    df['mesec_od'] = df['datum_od'].dt.month
    df['dan_od'] = df['datum_od'].dt.day
    df['ura_od'] = df['datum_od'].dt.hour
    df['min_od'] = df['datum_od'].dt.minute

    df['datum_do'] = pd.to_datetime(df['datum_do'])
    df['leto_do'] = df['datum_do'].dt.year
    df['mesec_do'] = df['datum_do'].dt.month
    df['dan_do'] = df['datum_do'].dt.day
    df['ura_do'] = df['datum_do'].dt.hour
    df['min_do'] = df['datum_do'].dt.minute

    # drop datum_od in datum_do
    df = df.drop(['datum_od'], axis=1)
    df = df.drop(['datum_do'], axis=1)


    df1 = df[df.isna().any(axis=1)]

    # fill missing data

    imp = IterativeImputer()
    imp.fit(df)
    temp_df = imp.transform(df)
    df = pd.DataFrame(temp_df, columns=df.columns)

    # kje si bomo shranili raw podatke
    filename = "data/processed/data.csv" 

    # ustvarimo folder in datoteko ce se ne obstaja
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    df.to_csv(filename, index=False)

def process_weather_data():
    timestr = time.strftime("%Y%m%d")
    # print(timestr)
    string = timestr+"*.json"
    # print(string)
    test = fnmatch.filter(os.listdir('data/raw/weather/'), string)
    # print(test[0])
    data = json.load(open('data/raw/weather/'+test[0]))
    # data1 = json.load(open('data/raw/weather/test2.json'))
    # print(data)
    df = pd.DataFrame(data['days'])
    print(df['datetime'])
    df_hours = df['hours']
    # print(df_hours)
    # print(df_hours[0])
    print(df_hours[6][23]['datetime'])
    print(df_hours[6][23]['temp'])
    # print(len(df_hours[0]))

    # zdruzimo datum in cas 
    date = str(df['datetime'][7]) 
    print(date)
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
                # print('i: ', i)
                # print('j: ', j)
                # print('date', date1)
                # print('time', time1)
                # print('temp', temp1)

    print(datetimes)
    print(temps)
    
    # preverimo ce se ujema
    print(datetimes[1])
    print(temps[1])

    print(df['datetime'][0])
    print(df_hours[0][1]['datetime'])
    print(df_hours[0][1]['temp'])

    df2 = pd.DataFrame()
    df2['datetime'] = datetimes
    df2['temps'] = temps

    print(df2)


    # for i in range(0,24):
    #     if i<10:
    #         print(date + "-0" + str(i) + ":00:00")
    #     else:
    #         print(date + "-" + str(i) + ":00:00")






    # timestr = time.strftime("%Y%m%d-%H%M%S")
    # filename = "data/raw/weather/test.json"
    # print("ok")
    # data_dict = pd.read_json(filename)
    # print(data_dict)
    # print(data_dict)
    # temp = data_dict['hourly']
    # print(temp[0]) # ure
    # print(temp[1][0]) # temps
    # print(len(temp[0]))
    # print(len(temp[1]))
    # filename = "data/processed/weather/" + timestr + ".json" 

    # ustvarimo folder in datoteko ce se ne obstaja
    # os.makedirs(os.path.dirname(filename), exist_ok=True)

    # df.to_csv(filename, index=False)