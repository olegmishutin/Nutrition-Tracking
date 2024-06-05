from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    is_superuser = models.BooleanField('является суперпользователем', default=False)
    is_staff = models.BooleanField('является админом', default=False)

    email = models.EmailField('email', unique=True, db_index=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'User'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
