from django.test import TestCase
from django.contrib.auth.models import User

from .models import ClientProfile


class ClientProfileTest(TestCase):

    def test_create_profile(self):

        user = User.objects.create_user(
            username='testuser',
            password='12345'
        )

        profile = ClientProfile.objects.create(
            user=user,
            phone='+375(29)111-11-11',
            age=25
        )

        self.assertEqual(
            profile.user.username,
            'testuser'
        )

        self.assertEqual(
            profile.age,
            25
        )