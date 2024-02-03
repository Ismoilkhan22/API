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
    username = models.CharField(max_length=128)
    email = models.ImageField(max_length=256, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CManager()
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'


class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField()
    img = models.ImageField(upload_to='imgs')
    like = models.ManyToManyField(User, related_name='like', blank=True)
