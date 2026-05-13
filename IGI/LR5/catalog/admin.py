from django.contrib import admin

from .models import (
    VehicleType,
    BodyType,
    CargoType,
    Vehicle
)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (
        'brand',
        'plate_number',
        'vehicle_type',
        'body_type',
        'load_capacity'
    )

    list_filter = (
        'vehicle_type',
        'body_type'
    )

    search_fields = (
        'brand',
        'plate_number'
    )


admin.site.register(VehicleType)
admin.site.register(BodyType)
admin.site.register(CargoType)