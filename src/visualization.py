import matplotlib.pyplot as plt


def plot_clusters(df):

    plt.figure(figsize=(8,6))

    plt.scatter(
        df["Income"],
        df["SpendingScore"],
        c=df["Cluster"],
        s=80
    )

    plt.xlabel("Income")

    plt.ylabel("Spending Score")

    plt.title("Customer Segmentation")

    plt.grid(True)

    plt.savefig("images/result.png")

    plt.show()