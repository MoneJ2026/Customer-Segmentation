import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("data/customers.csv")

# Select features
X = df[["Income", "SpendingScore"]]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(X_scaled[:5])