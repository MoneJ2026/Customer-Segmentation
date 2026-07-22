from src.preprocess import load_data, preprocess
from src.clustering import train_model
from src.visualization import plot_clusters

df = load_data("data/customers.csv")

X = preprocess(df)

model = train_model(X)

df["Cluster"] = model.labels_

plot_clusters(df)

df.to_csv(
    "output/customer_clusters.csv",
    index=False
)

print("Finished Successfully")