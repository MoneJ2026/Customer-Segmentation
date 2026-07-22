from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def elbow_method(X):

    errors = []

    for k in range(1, 11):

        model = KMeans(
            n_clusters=k,
            random_state=42
        )

        model.fit(X)

        errors.append(model.inertia())

    plt.figure(figsize=(8,5))

    plt.plot(range(1,11), errors, marker="o")

    plt.xlabel("Clusters")

    plt.ylabel("Inertia")

    plt.title("Elbow Method")

    plt.grid(True)

    plt.savefig("images/elbow.png")

    plt.show()