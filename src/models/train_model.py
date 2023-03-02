import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, explained_variance_score
import os
import h5py
import joblib

def train_models():
    filename = "data/processed/data.csv" 
    df = pd.read_csv(filename)
    # print(df)

    # print(df.isnull().sum())

    columns = df.columns
    vhod = columns.tolist()
    vhod.remove('pm10')

    # print(vhod)

    X_train, X_test, y_train, y_test = train_test_split(df[vhod], df['pm10'], test_size=0.3, random_state=1234)

    reg = LinearRegression()
    reg.fit(X_train, y_train)

    train_pred = reg.predict(X_train)
    test_pred = reg.predict(X_test)

    # print(reg.score(X_test, y_test))

    filename = 'models/model1.joblib' 
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