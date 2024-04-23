from django.contrib.auth.models import User, AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Пользовательская модель User с авторизацией по полям email и password
    """
    username = None
    email = models.EmailField("email адрес", unique=True)

    patronymic = models.CharField(verbose_name='Отчество', max_length=150, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['last_name', 'first_name', 'patronymic']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{str(self.last_name).capitalize()} " \
               f"{str(self.first_name).capitalize()} " \
               f"{str(self.patronymic).capitalize()}".strip()

    def get_short_name(self):
        return f"{str(self.last_name).capitalize()} " \
               f"{str(self.first_name).capitalize()} ".strip()


