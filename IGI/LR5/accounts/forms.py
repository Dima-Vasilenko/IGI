from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from datetime import date

from .models import DriverProfile, ClientProfile


class RegisterForm(UserCreationForm):

    ROLE_CHOICES = [
        ('driver', 'Водитель'),
        ('client', 'Клиент'),
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES
    )

    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date'
        })
    )

    phone = forms.CharField()

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'role',
            'birth_date',
            'phone',
        ]

    def clean_birth_date(self):

        birth_date = self.cleaned_data['birth_date']

        today = date.today()

        age = (
            today.year
            - birth_date.year
            - (
                (today.month, today.day)
                < (birth_date.month, birth_date.day)
            )
        )

        if age < 18:
            raise ValidationError(
                'Пользователь должен быть старше 18 лет'
            )

        return birth_date

    def save(self, commit=True):

        user = super().save(commit=True)

        role = self.cleaned_data['role']

        birth_date = self.cleaned_data['birth_date']

        phone = self.cleaned_data['phone']

        if role == 'driver':

            DriverProfile.objects.create(
                user=user,
                birth_date=birth_date,
                phone=phone,
                experience_years=0,
                license_category='B'
            )

        else:

            ClientProfile.objects.create(
                user=user,
                birth_date=birth_date,
                phone=phone
            )

        return user