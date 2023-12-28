# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.db import models
#
#
# class CustomUser(AbstractUser):
#     profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         if not email:
#             raise ValueError("Email is required")
#         if not username:
#             raise ValueError("Username is required")
#
#         user = self.model(
#             username=username,
#             email=self.normalize_email(email),
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, email, password=None):
#         if not email:
#             raise ValueError("Email is required")
#         if not username:
#             raise ValueError("Username is required")
#
#         user = self.model(
#             username=username,
#             email=self.normalize_email(email),
#         )
#
#         user.set_password(password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
