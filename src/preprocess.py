import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(path):
    return pd.read_csv(path)


def preprocess(df):
    X = df[["Income", "SpendingScore"]]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled