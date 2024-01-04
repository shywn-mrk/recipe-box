from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View

from .forms import CustomUserCreationForm, UserProfileForm

User = get_user_model()


class CustomRegistrationView(CreateView):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")


class CustomPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset.html"
    email_template_name = "accounts/password_reset_email.txt"


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("recipes:list")


class ProfileView(LoginRequiredMixin, View):
    template_name = "accounts/profile.html"

    def get(self, request, *args, **kwargs):
        user_profile = (
            User.objects.filter(pk=request.user.pk)
            .values("username", "email")
            .first()
        )
        return render(
            request, self.template_name, {"user_profile": user_profile}
        )


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)
