from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=255)

    short_description = models.TextField()

    full_text = models.TextField()

    image = models.ImageField(
        upload_to='news/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=255)

    answer = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Vacancy(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):

    RATE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    rating = models.IntegerField(
        choices=RATE_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}"


class PromoCode(models.Model):
    code = models.CharField(max_length=50)

    discount_percent = models.IntegerField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


class ContactEmployee(models.Model):
    full_name = models.CharField(max_length=255)

    position = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    email = models.EmailField()

    photo = models.ImageField(
        upload_to='employees/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.full_name


class CompanyInfo(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    founded_year = models.IntegerField()

    def __str__(self):
        return self.title