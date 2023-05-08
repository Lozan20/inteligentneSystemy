import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from .models import Car, Repair


def preprocess_data():
    """
    Preprocess data from the database by cleaning, encoding and normalizing it.

    Returns:
    pd.DataFrame: Preprocessed data in the form of a pandas DataFrame.
    """
    repairs = Repair.objects.all()

    data = []
    for repair in repairs:
        data.append(
            [
                repair.car.brand,
                repair.car.model,
                repair.car.year,
                repair.repair_date.strftime("%Y%m%d"),
                repair.replaced_part,
                repair.part_cost,
                repair.official_part_lifetime,
            ]
        )

    df = pd.DataFrame(
        data,
        columns=[
            "brand",
            "model",
            "year",
            "repair_date",
            "replaced_part",
            "part_cost",
            "official_part_lifetime",
        ],
    )

    # Usuwanie brakujących wartości
    df = df.dropna()

    # Kodowanie danych kategorycznych
    # Kodowanie danych kategorycznych
    le = LabelEncoder()
    df["brand"] = le.fit_transform(df["brand"])
    df["model"] = le.fit_transform(df["model"])
    df["replaced_part"] = le.fit_transform(df["replaced_part"])

    # Normalizacja danych liczbowych
    scaler = MinMaxScaler()
    df[["year", "part_cost", "official_part_lifetime"]] = scaler.fit_transform(
        df[["year", "part_cost", "official_part_lifetime"]]
    )

    return df
