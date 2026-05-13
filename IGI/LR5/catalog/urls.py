from django.urls import path, re_path

from . import views


urlpatterns = [

    path(
        'vehicles/',
        views.vehicle_list
    ),

    path(
        'vehicles/create/',
        views.vehicle_create
    ),

    re_path(
        r'^vehicles/(?P<pk>\d+)/update/$',
        views.vehicle_update
    ),

    re_path(
        r'^vehicles/(?P<pk>\d+)/delete/$',
        views.vehicle_delete
    ),
]