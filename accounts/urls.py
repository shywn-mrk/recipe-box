from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (
    CustomPasswordResetDoneView,
    CustomPasswordResetView,
    CustomRegistrationView,
)

app_name = "accounts"
urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", CustomRegistrationView.as_view(), name="register"),
    path(
        "password_reset/",
        CustomPasswordResetView.as_view(),
        name="password-reset",
    ),
    path(
        "password_reset_done/",
        CustomPasswordResetDoneView.as_view(),
        name="password-reset-done",
    ),
]
