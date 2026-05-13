from django.contrib import admin

from .models import (
    News,
    FAQ,
    Review,
    Vacancy,
    PromoCode,
    ContactEmployee,
    CompanyInfo
)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'created_at'
    )

    search_fields = (
        'title',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'rating',
        'created_at'
    )

    list_filter = (
        'rating',
    )


admin.site.register(FAQ)
admin.site.register(Vacancy)
admin.site.register(PromoCode)
admin.site.register(ContactEmployee)
admin.site.register(CompanyInfo)