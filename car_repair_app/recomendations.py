from .data_processing import preprocess_data
from .inference import find_best_k, train_knn_classifier, make_prediction


def generate_recommendations():
    """
    Generate recommendations for car parts using K-NN classifier.

    Returns:
    list: List of recommendations for car parts.
    """
    df = preprocess_data()
    labels = df.pop("replaced_part")
    k_range = range(1, 11)

    best_k = find_best_k(df, labels, k_range)
    knn = train_knn_classifier(df, labels, n_neighbors=best_k)

    # Dodaj nowe dane do predykcji (np. dane klienta)
    new_data = ...
    prediction = make_prediction(knn, new_data)

    # Przekształć predykcję na czytelną listę rekomendacji
    recommendations = ...

    return recommendations
