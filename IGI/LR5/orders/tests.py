from django.test import TestCase

from django.contrib.auth.models import User

from accounts.models import ClientProfile

from catalog.models import (
    VehicleType,
    BodyType,
    CargoType,
    Vehicle
)

from .models import Order


class OrderModelTest(TestCase):

    def setUp(self):

        user = User.objects.create_user(
            username='testuser',
            password='12345'
        )

        client = ClientProfile.objects.create(
            user=user,
            birth_date='2000-10-10',
            phone='+375 (29) 123-45-67'
        )

        vehicle_type = VehicleType.objects.create(
            name='Truck'
        )

        body_type = BodyType.objects.create(
            name='Tent'
        )

        cargo_type = CargoType.objects.create(
            name='Food'
        )

        vehicle = Vehicle.objects.create(
            brand='MAN',
            plate_number='1234 AB-7',
            vehicle_type=vehicle_type,
            body_type=body_type,
            load_capacity=10
        )

        self.order = Order.objects.create(
            client=client,
            vehicle=vehicle,
            cargo_type=cargo_type,
            cargo_weight=5,
            pickup_address='Минск',
            delivery_address='Гродно',
            price=1000
        )

    def test_order_created(self):

        self.assertEqual(
            self.order.price,
            1000
        )

    def test_order_status(self):

        self.assertEqual(
            self.order.status,
            'new'
        )