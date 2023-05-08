import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from .data_processing import preprocess_data

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_knn_classifier(data, labels, n_neighbors=5):
    """
    Train K-NN classifier on the given data.

    Args:
    data (pd.DataFrame): Data to train the classifier on.
    labels (pd.Series): Labels associated with the data.
    n_neighbors (int, optional): Number of neighbors to use for classification. Defaults to 5.

    Returns:
    KNeighborsClassifier: Trained K-NN classifier.
    """
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(data, labels)
    return knn


def make_prediction(knn, new_data):
    """
    Make a prediction using the trained K-NN classifier.

    Args:
    knn (KNeighborsClassifier): Trained K-NN classifier.
    new_data (np.array): New input data to make predictions.

    Returns:
    int: Predicted label for the new data.
    """
    # Ensure the input data is a 2D array
    new_data = np.array(new_data).reshape(1, -1)
    prediction = knn.predict(new_data)
    return prediction


def find_best_k(data, labels, k_range):
    """
    Find the optimal k value for K-NN classifier.

    Args:
    data (pd.DataFrame): Data to train the classifier on.
    labels (pd.Series): Labels associated with the data.
    k_range (range): Range of k values to test.

    Returns:
    int: Optimal k value.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        data, labels, test_size=0.3, random_state=42
    )

    best_k = 0
    best_score = 0

    for k in k_range:
        knn = train_knn_classifier(X_train, y_train, n_neighbors=k)
        y_pred = make_prediction(knn, X_test)
        score = accuracy_score(y_test, y_pred)

        if score > best_score:
            best_score = score
            best_k = k

    return best_k
