from sklearn.metrics import silhouette_score


def evaluate_model(X, labels):

    score = silhouette_score(X, labels)

    print("=" * 40)
    print("Silhouette Score")
    print(score)
    print("=" * 40)