from sklearn.metrics import silhouette_score


def evaluate_model(X, labels):

    score = silhouette_score(X, labels)

    print("=" * 40)
    print(f"Silhouette Score: {score:.3f}")
    print("=" * 40)