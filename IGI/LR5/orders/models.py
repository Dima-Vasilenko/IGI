from django.db import models

from accounts.models import DriverProfile, ClientProfile
from catalog.models import Vehicle, Service, CargoType


class Order(models.Model):

    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершен'),
    ]

    client = models.ForeignKey(
        ClientProfile,
        on_delete=models.CASCADE
    )

    driver = models.ForeignKey(
        DriverProfile,
        on_delete=models.SET_NULL,
        null=True
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True
    )

    cargo_type = models.ForeignKey(
        CargoType,
        on_delete=models.SET_NULL,
        null=True
    )

    services = models.ManyToManyField(Service)

    cargo_weight = models.FloatField()

    pickup_address = models.CharField(max_length=255)

    delivery_address = models.CharField(max_length=255)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Заказ #{self.id}"