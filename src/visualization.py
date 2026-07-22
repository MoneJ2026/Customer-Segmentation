import matplotlib.pyplot as plt
import os

def plot_clusters(df):

    os.makedirs("images", exist_ok=True)

    plt.figure(figsize=(8,6))

    plt.scatter(
        df["Income"],
        df["SpendingScore"],
        c=df["Cluster"]
    )

    plt.xlabel("Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segmentation")

    plt.savefig("images/result.png")

    plt.show()