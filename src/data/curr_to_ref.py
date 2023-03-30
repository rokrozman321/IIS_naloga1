import pandas as pd

def curr_to_ref():
    df = pd.read_csv('data/processed/current_data.csv')
    df1 = pd.read_csv('data/processed/reference_data.csv')
    # print(df1)
    df.to_csv('data/processed/reference_data.csv', index=False)
    # print("Po kopiranju")

    # df1 = pd.read_csv('data/processed/reference_data.csv')
    # print(df1)

curr_to_ref()