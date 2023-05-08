from django.db import models


class Car(models.Model):
    """
    Model representing a car.
    """

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Repair(models.Model):
    """
    Model representing a car repair record.
    """

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    repair_date = models.DateField()
    replaced_part = models.CharField(max_length=100)
    part_cost = models.FloatField()
    official_part_lifetime = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.car} - {self.repair_date} - {self.replaced_part}"
