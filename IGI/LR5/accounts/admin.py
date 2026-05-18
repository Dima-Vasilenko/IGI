from django.contrib import admin

from .models import (
    ClientProfile,
    Organization,
    DriverProfile
)


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'birth_date',
        'phone'
    )

    search_fields = (
        'user__username',
        'phone'
    )

admin.site.register(Organization)
admin.site.register(DriverProfile)