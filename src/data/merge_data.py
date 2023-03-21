import json
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import os
import pandas as pd
import time
from datetime import datetime

import fnmatch

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

merge_data()