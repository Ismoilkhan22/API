from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import UserManager, PermissionsMixin


class CManager(UserManager):
    def create_user(self, email=None, password=None, is_superuser=False, is_staff=False, **extra_fields):
        user = self.model(
            email=email,
            password=password,
            is_superuser=is_superuser,
            is_staff=is_staff,
            **extra_fields

        )
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, email=None, password=None, is_superuser=False, is_staff=False, **extra_fields):
        return self.create_user(
            email=email,
            password=password,
            is_superuser=is_superuser,
            is_staff=is_staff,
            **extra_fields

        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.ImageField(max_length=256, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'


