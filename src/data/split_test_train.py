import pandas as pd

def split_data():
    df = pd.read_csv('data/processed/current_data.csv')
    # print(df)
    test_idx = int(len(df) * 0.1)
    print(test_idx)
    train_df = df.iloc[test_idx:]
    test_df = df.iloc[:test_idx]
    print(train_df)
    print(test_df)
    train_df.to_csv('data/processed/train_data.csv', index=False)
    test_df.to_csv('data/processed/test_data.csv', index=False)

split_data()