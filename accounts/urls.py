from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (
    CustomPasswordChangeView,
    CustomPasswordResetDoneView,
    CustomPasswordResetView,
    CustomRegistrationView,
    EditProfileView,
    ProfileView,
)

app_name = "accounts"
urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("edit_profile/", EditProfileView.as_view(), name="edit-profile"),
    path("register/", CustomRegistrationView.as_view(), name="register"),
    path(
        "password_change/",
        CustomPasswordChangeView.as_view(),
        name="password-change",
    ),
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
