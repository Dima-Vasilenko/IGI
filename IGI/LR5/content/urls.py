from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list),
    path('faq/', views.faq_list),
    path('vacancies/', views.vacancy_list),
    path('reviews/', views.review_list),
    path('reviews/add/', views.add_review),
    path('random-driver/', views.random_driver),
    path('currency/', views.currency_rates),
    path('contacts/', views.contacts_view),
    path('company/', views.company_view),
]