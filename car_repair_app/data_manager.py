import pandas as pd
from .models import Repair

from django.test import TestCase
from .data_manager import clean_data


def get_car_parts_data():
    """
    Get car parts data from the database.

    Returns:
    pd.DataFrame: Car parts data in a pandas DataFrame format.
    """
    car_parts_data = Repair.objects.values()

    if not car_parts_data:
        return None

    df = pd.DataFrame.from_records(car_parts_data)
    return df


class DataManagerTest(TestCase):
    def test_clean_data(self):
        # Arrange
        data = [
            [1, "Audi", "2021", "brake", "100.0", "30000"],
            [2, "BMW", "2019", "tires", "200.0", "40000"],
        ]

        expected_result = [[1, 0, 0.0, 1.0], [2, 1, 0.5, 0.5]]

        # Act
        cleaned_data = clean_data(data)

        # Assert
        self.assertEqual(cleaned_data, expected_result)
