from sklearn.cluster import KMeans


def train_model(X):

    model = KMeans(
        n_clusters=5,
        random_state=42
    )

    model.fit(X)

    return model