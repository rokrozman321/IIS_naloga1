import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, explained_variance_score
import os
import h5py
import joblib

import mlflow
# from utils import fetch_logged_data
from pprint import pprint

def train_models():
    print("Train model")
    filename = 'data/processed/merged.csv'
    df = pd.read_csv(filename)
    # print(df)

    df['time'] = pd.to_datetime(df['datetime'])
    df.sort_values(by='time', inplace=True)
    df = df.drop(['datetime'], axis=1)
    # print(df)
    df = df.drop(['time'], axis=1)
    # print(df)

    X = df[['pm2.5', 'o3', 'no2', 'temps']]
    y = df['pm10']

    # print(X)
    # print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

    reg = LinearRegression()
    reg.fit(X_train, y_train)

    train_pred = reg.predict(X_train)
    test_pred = reg.predict(X_test)

    # print(reg.score(X_test, y_test))

    filename = 'models/model2.joblib' 
    # ustvarimo folder in datoteko ce se ne obstaja
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    joblib.dump(reg, filename)

    filename = 'reports/train_metrics.txt' 
    # ustvarimo folder in datoteko ce se ne obstaja
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    train_mae = mean_absolute_error(y_train, train_pred)
    # print(train_mae)

    train_mse = mean_squared_error(y_train, train_pred)
    # print(train_mse)

    train_evs = explained_variance_score(y_train, train_pred)
    # print(train_evs)

    # reports/metrics.txt
    filename = 'reports/metrics.txt' 
    # ustvarimo folder in datoteko ce se ne obstaja
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    test_mae = mean_absolute_error(y_test, test_pred)
    # print(test_mae)

    test_mse = mean_squared_error(y_test, test_pred)
    # print(test_mse)

    test_evs = explained_variance_score(y_test, test_pred)
    # print(test_evs)

    with open("reports/train_metrics.txt", "w") as f:
        f.write(f"Train mae: {train_mae:.4f}\nTrain mse: {train_mse:.4f}\nTrain evs: {train_evs:.4f}")

    with open("reports/metrics.txt", "w") as f:
        f.write(f"Test mae: {test_mae:.4f}\nTest mse: {test_mse:.4f}\nTest evs: {test_evs:.4f}")

# train_models()

def train_model2():

    MLFLOW_TRACKING_URI="https://dagshub.com/rokrozman321/IIS_naloga1.mlflow"
    # MLFLOW_TRACKING_USERNAME=rokrozman321
    # MLFLOW_TRACKING_PASSWORD=5e0bc28a77878c6c315d7d1f8ac30a58f611f7fa
    # python script.py
    print("Train model 2")
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment("IIS1")

    # enable autologging
    mlflow.sklearn.autolog()

    filename = 'data/processed/train_data.csv'
    df = pd.read_csv(filename)
    filename = 'data/processed/test_data.csv'
    df_test = pd.read_csv(filename)
    # print(df)
    # print(df_test)
    df['time'] = pd.to_datetime(df['datetime'])
    df.sort_values(by='time', inplace=True)
    df = df.drop(['datetime'], axis=1)
    print(df)
    df = df.drop(['time'], axis=1)
    print(df)
    
    X_train = df[['pm2.5', 'o3', 'no2', 'temps']]
    y_train = df['pm10']

    # print(X_train)
    # print("---------------------------")
    # print(y_train)

    X_test = df_test[['pm2.5', 'o3', 'no2', 'temps']]
    y_test = df_test['pm10']

    # print(X_test)
    # print("---------------------------")
    # print(y_test)

    reg = LinearRegression()
    reg.fit(X_train, y_train)

    run_id = mlflow.last_active_run().info.run_id
    print("Logged data and model in run {}".format(run_id))
    # show logged data
    # for key, data in fetch_logged_data(run_id).items():
    # print(r)
    # print("\n---------- logged {} ----------".format(run_id.key))
    # pprint(run_id.data)

    # train_pred = reg.predict(X_train)
    # test_pred = reg.predict(X_test)

    # # print(reg.score(X_test, y_test))

    # filename = 'models/model2.joblib' 
    # # ustvarimo folder in datoteko ce se ne obstaja
    # os.makedirs(os.path.dirname(filename), exist_ok=True)

    # joblib.dump(reg, filename)

    # filename = 'reports/train_metrics.txt' 
    # # ustvarimo folder in datoteko ce se ne obstaja
    # os.makedirs(os.path.dirname(filename), exist_ok=True)

    # train_mae = mean_absolute_error(y_train, train_pred)
    # # print(train_mae)

    # train_mse = mean_squared_error(y_train, train_pred)
    # # print(train_mse)

    # train_evs = explained_variance_score(y_train, train_pred)
    # # print(train_evs)

    # # reports/metrics.txt
    # filename = 'reports/metrics.txt' 
    # # ustvarimo folder in datoteko ce se ne obstaja
    # os.makedirs(os.path.dirname(filename), exist_ok=True)

    # test_mae = mean_absolute_error(y_test, test_pred)
    # # print(test_mae)

    # test_mse = mean_squared_error(y_test, test_pred)
    # # print(test_mse)

    # test_evs = explained_variance_score(y_test, test_pred)
    # # print(test_evs)

    # with open("reports/train_metrics.txt", "w") as f:
    #     f.write(f"Train mae: {train_mae:.4f}\nTrain mse: {train_mse:.4f}\nTrain evs: {train_evs:.4f}")

    # with open("reports/metrics.txt", "w") as f:
    #     f.write(f"Test mae: {test_mae:.4f}\nTest mse: {test_mse:.4f}\nTest evs: {test_evs:.4f}")



train_model2()