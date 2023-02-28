import pandas as pd
import json
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


filename = "data/raw/data.json"
data_dict = pd.read_json(filename)

d = []

print(data_dict)
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
print(df)

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


print(df)

# drop datum_od in datum_do
df = df.drop(['datum_od'], axis=1)
df = df.drop(['datum_do'], axis=1)

# missing data
print(df.isnull().sum())

# df=df.fillna(method='ffill')
# print(df.isnull().sum())
# print(df)


df1 = df[df.isna().any(axis=1)]
print (df1)

# fill missing data

imp = IterativeImputer()
imp.fit(df)
temp_df = imp.transform(df)
df = pd.DataFrame(temp_df, columns=df.columns)

print(df)
print(df.isnull().sum())

