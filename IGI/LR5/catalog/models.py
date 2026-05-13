from django.db import models


class VehicleType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BodyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CargoType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    brand = models.CharField(max_length=100)

    plate_number = models.CharField(max_length=20)

    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.CASCADE
    )

    body_type = models.ForeignKey(
        BodyType,
        on_delete=models.CASCADE
    )

    cargo_types = models.ManyToManyField(CargoType)

    load_capacity = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} ({self.plate_number})"