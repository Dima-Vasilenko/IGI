from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    register_view,
    profile_view,
    logout_view
)

urlpatterns = [

    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    path(
        'register/',
        register_view,
        name='register'
    ),

    path(
        'profile/',
        profile_view,
        name='profile'
    ),
]