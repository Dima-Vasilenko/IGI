from django.urls import path, re_path

from . import views


urlpatterns = [

    path(
        'orders/',
        views.order_list
    ),

    path(
        'orders/create/',
        views.order_create
    ),

    re_path(
        r'^orders/(?P<pk>\d+)/update/$',
        views.order_update
    ),

    re_path(
        r'^orders/(?P<pk>\d+)/delete/$',
        views.order_delete
    ),

    path(
        'statistics/',
        views.statistics_view
    ),
]