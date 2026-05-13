from django.contrib import admin

from .models import (
    Order,
    Service
)


class ServiceInline(admin.TabularInline):

    model = Order.services.through

    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'client',
        'vehicle',
        'price',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'cargo_type'
    )

    search_fields = (
        'client__user__username',
        'vehicle__brand'
    )

    inlines = [ServiceInline]


admin.site.register(Service)