
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def elbow_method(X):

    errors = []

    for k in range(1, 11):

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(X)

        errors.append(model.inertia_)

    plt.figure(figsize=(8, 5))

    plt.plot(
        range(1, 11),
        errors,
        marker="o"
    )

    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Inertia")
    plt.title("Elbow Method")

    plt.grid(True)

    plt.savefig("images/elbow.png")

    plt.show()


def train_model(X):

    model = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )

    model.fit(X)

    return model

