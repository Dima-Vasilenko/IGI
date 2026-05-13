from django.test import TestCase

from .models import (
    VehicleType,
    BodyType,
    Vehicle
)


class VehicleTest(TestCase):

    def test_create_vehicle(self):

        vehicle_type = VehicleType.objects.create(
            name='Truck'
        )

        body_type = BodyType.objects.create(
            name='Closed'
        )

        vehicle = Vehicle.objects.create(
            brand='MAN',
            plate_number='1234 AB-7',
            load_capacity=20,
            vehicle_type=vehicle_type,
            body_type=body_type
        )

        self.assertEqual(
            vehicle.brand,
            'MAN'
        )