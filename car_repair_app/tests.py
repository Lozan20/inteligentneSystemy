import unittest
import numpy as np
from .data_manager import normalize_data


class TestDataNormalization(unittest.TestCase):
    def test_normalize_data_scalar_input(self):
        input_data = 2.5
        expected_output = np.array([[-1.30650493]])
        self.assertTrue(np.allclose(normalize_data(input_data), expected_output))

    def test_normalize_data_1d_array_input(self):
        input_data = np.array([1, 2, 3])
        expected_output = np.array([[-1.22474487, -0.0, 1.22474487]])
        self.assertTrue(np.allclose(normalize_data(input_data), expected_output))

    def test_normalize_data_2d_array_input(self):
        input_data = np.array([[1, 2, 3], [4, 5, 6]])
        expected_output = np.array(
            [[-1.34164079, -0.4472136, 0.4472136], [0.4472136, 1.34164079, 2.23606798]]
        )
        self.assertTrue(np.allclose(normalize_data(input_data), expected_output))

    def test_normalize_data_3d_array_input(self):
        input_data = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
        expected_output = np.array(
            [
                [
                    [-1.34164079, -0.4472136, 0.4472136],
                    [0.4472136, 1.34164079, 2.23606798],
                ],
                [
                    [3.13049517, 3.91767291, 4.70485064],
                    [5.49202837, 6.27920611, 7.06638384],
                ],
            ]
        )
        self.assertTrue(np.allclose(normalize_data(input_data), expected_output))

    def test_normalize_data_empty_input(self):
        input_data = np.array([])
        with self.assertRaises(ValueError):
            normalize_data(input_data)

    def test_normalize_data_non_numeric_input(self):
        input_data = "invalid"
        with self.assertRaises(TypeError):
            normalize_data(input_data)

    def test_normalize_data_nan_input(self):
        input_data = np.array([1, 2, np.nan])
        with self.assertRaises(ValueError):
            normalize_data(input_data)

    def test_normalize_data_inf_input(self):
        input_data = np.array([1, 2, np.inf])
        with self.assertRaises(ValueError):
            normalize_data(input_data)

    def test_normalize_data_n_features_mismatch(self):
        input_data = np.array([[1, 2, 3], [4, 5, 6]])
        scaler = StandardScaler().fit(np.array([[1, 2], [4, 5]]))
        with self.assertRaises(ValueError):
            normalize_data(input_data, scaler=scaler)

    def test_normalize_data_custom_scaler(self):
        input_data = np.array([[1, 2, 3], [4, 5, 6]])
        scaler = MinMaxScaler().fit(input_data)
        expected_output = np.array([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]])
        self.assertTrue(
            np.allclose(normalize_data(input_data, scaler=scaler), expected_output)
        )

    def test_encode_column():
        data = {"model": ["Focus", "Civic", "Corolla"]}
        df = pd.DataFrame(data)
        encoded = encode_column(df, "model")
        expected = {0: {"Corolla": 2, "Civic": 1, "Focus": 0}}
        assert encoded == expected

    def test_normalize_data():
        data = {"cost": [100, 200, 300], "lifetime": [10, 20, 30]}
        df = pd.DataFrame(data)
        normalized = normalize_data(df)
        expected = pd.DataFrame({"cost": [0.0, 0.5, 1.0], "lifetime": [0.0, 0.5, 1.0]})
        pd.testing.assert_frame_equal(normalized, expected)

    def test_knn_prediction():
        X_train = pd.DataFrame({"cost": [100, 200, 300], "lifetime": [10, 20, 30]})
        y_train = pd.Series(["brake", "engine", "brake"])
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(X_train, y_train)
        X_test = pd.DataFrame({"cost": [250], "lifetime": [18]})
        prediction = knn.predict(X_test)
        expected = ["engine"]
        assert np.array_equal(prediction, expected)

    def test_prediction_in_choices():
        choices = ["brake", "engine", "transmission"]
        prediction = predict_repair("Ford", "Focus", 2010, 150000, 100, 10, choices)
        assert prediction in choices

    def test_data_processing_speed():
        data = generate_random_data(10000)
        start = time.time()
        df = process_data(data)
        end = time.time()
        time_elapsed = end - start
        assert time_elapsed < 10.0  # expected processing time < 10 seconds
