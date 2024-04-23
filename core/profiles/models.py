from django.core.validators import RegexValidator
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
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    role = models.PositiveSmallIntegerField(verbose_name='Роль',
                                            choices=USER_ROLE_CHOICES, default=CLIENT)
    phone_regex = RegexValidator(regex=r'^(\+7)\s?\(?[489][0-9]{2}\)\s?[0-9]{3}\-[0-9]{2}\-[0-9]{2}$',
                                 message="Телефон должен иметь 18 символов и следующий формат: '+7 (999) 999-99-99'.")
    phone_number = models.CharField(verbose_name='Номер телефона', validators=[phone_regex],
                                    max_length=18, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user.get_short_name()}'


class Company(models.Model):
    """
    Модель описывающая компанию в которой работал пользователь(заглушка).
    """
    title = models.CharField(verbose_name='Название', max_length=150)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    """
    Модель описывающая опыт работы пользователя.
    У 1 пользователя может быть много компаний в которых он работал/работает.
    """
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE, verbose_name='Профиль')
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, verbose_name='Компания')
    description = models.CharField(verbose_name='Описание деятельности', max_length=255, default='')
    start_date = models.DateField(verbose_name='Начало работы')
    end_date = models.DateField(verbose_name='Окончание работы', null=True, blank=True)

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работ'

    def __str__(self):
        return f'{self.profile} - {self.company}'

