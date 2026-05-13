from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator


phone_validator = RegexValidator(
    regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
    message='Формат: +375 (29) XXX-XX-XX'
)


class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)]
    )

    phone = models.CharField(
        max_length=20,
        validators=[phone_validator]
    )

    experience_years = models.PositiveIntegerField(default=0)

    license_category = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)]
    )

    phone = models.CharField(
        max_length=20,
        validators=[phone_validator]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username