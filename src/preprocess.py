import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(path):
    df = pd.read_csv(path)
    return df


def preprocess(df):
    X = df[["Income", "SpendingScore"]]

    scaler = StandardScaler()

    X = scaler.fit_transform(X)

    return X