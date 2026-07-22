import os

from src.preprocess import load_data, preprocess
from src.clustering import train_model, elbow_method
from src.visualization import plot_clusters
from src.evaluation import evaluate_model

os.makedirs("images", exist_ok=True)
os.makedirs("output", exist_ok=True)

df = load_data("data/customers.csv")

X = preprocess(df)

elbow_method(X)

model = train_model(X)

df["Cluster"] = model.labels_

evaluate_model(X, model.labels_)

plot_clusters(df)

df.to_csv(
    "output/customer_clusters.csv",
    index=False
)

print("Project Finished Successfully")