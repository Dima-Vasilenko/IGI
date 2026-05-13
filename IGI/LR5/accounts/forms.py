from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import DriverProfile, ClientProfile


class RegisterForm(UserCreationForm):

    ROLE_CHOICES = [
        ('driver', 'Водитель'),
        ('client', 'Клиент'),
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES
    )

    age = forms.IntegerField()

    phone = forms.CharField()

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'role',
            'age',
            'phone',
        ]

    def save(self, commit=True):

        user = super().save(commit=True)

        role = self.cleaned_data['role']

        age = self.cleaned_data['age']

        phone = self.cleaned_data['phone']

        if role == 'driver':

            DriverProfile.objects.create(
                user=user,
                age=age,
                phone=phone,
                experience_years=0,
                license_category='B'
            )

        else:

            ClientProfile.objects.create(
                user=user,
                age=age,
                phone=phone
            )

        return user