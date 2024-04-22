from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


CLIENT = 1
EXECUTOR = 2

USER_ROLE_CHOICES = (
      (CLIENT, 'Заказчик'),
      (EXECUTOR, 'Исполнитель'),
)


class Profile(models.Model):
    """
    Модель описывающая профиль пользователя.
    """
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(verbose_name='Роль',
                                            choices=USER_ROLE_CHOICES, default=CLIENT)

    last_name = models.CharField(verbose_name='Фамилия', max_length=150, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=150, blank=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=150, blank=True)


class Company(models.Model):
    """
    Модель описывающая компанию в которой работал пользователь(заглушка).
    """
    title = models.CharField(verbose_name='Название', max_length=150)


class WorkExperience(models.Model):
    """
    Модель описывающая опыт работы пользователя.
    У 1 пользователя может быть много компаний в которых он работал/работает.
    """
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='Начало работы')
    end_date = models.DateField(verbose_name='Окончание работы', null=True, blank=True)

