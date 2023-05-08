import random
from .models import Car, Repair
from django.utils import timezone


def generate_random_data(number_of_records):
    """
    Generate random car and repair records and save them to the database.

    Args:
    number_of_records (int): Number of records to generate.
    """
    brands = ["Toyota", "Ford", "Volkswagen", "Honda", "BMW"]
    models = ["Model A", "Model B", "Model C", "Model D", "Model E"]
    parts = ["Engine", "Brake Pad", "Exhaust", "Transmission", "Suspension"]

    for _ in range(number_of_records):
        car = Car(
            brand=random.choice(brands),
            model=random.choice(models),
            year=random.randint(2000, 2021),
        )
        car.save()

        repair = Repair(
            car=car,
            repair_date=timezone.now()
            - timezone.timedelta(days=random.randint(1, 1000)),
            replaced_part=random.choice(parts),
            part_cost=random.uniform(50, 1000),
            official_part_lifetime=random.randint(5000, 100000),
        )
        repair.save()
