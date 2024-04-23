# Generated by Django 5.0.4 on 2024-04-23 03:05

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Заказчик'), (2, 'Исполнитель')], default=1, verbose_name='Роль')),
                ('phone_number', models.CharField(blank=True, max_length=18, unique=True, validators=[django.core.validators.RegexValidator(message="Телефон должен иметь 18 символов и следующий формат: '+7 (999) 999-99-99'.", regex='^(\\+7)\\s?\\(?[489][0-9]{2}\\)\\s?[0-9]{3}\\-[0-9]{2}\\-[0-9]{2}$')], verbose_name='Номер телефона')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Начало работы')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Окончание работы')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.company')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]