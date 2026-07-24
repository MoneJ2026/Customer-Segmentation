import matplotlib.pyplot as plt


def plot_clusters(df):

    plt.figure(figsize=(8,6))

    plt.scatter(
        df["Income"],
        df["SpendingScore"],
        c=df["Cluster"],
        cmap="rainbow",
        s=100
    )

    plt.xlabel("Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segmentation")

    plt.savefig("images/result.png")

    plt.show()