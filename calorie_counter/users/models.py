from django.db import models
from datetime import date


class User(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=20, blank=True)
    email = models.EmailField(verbose_name='e-mail', blank=True)
    password = models.CharField(verbose_name='Пароль', max_length=20, blank=True)
    birth_date = models.DateField(verbose_name='Дата рождения', default=date(2000, 1, 1))
    height = models.IntegerField(verbose_name='Рост')
    weight = models.IntegerField(verbose_name='Вес')

    MAN = 'MAN'
    WOMAN = 'WOMAN'
    GENDER_CHOICES = [
        (MAN, 'Мужчина'),
        (WOMAN, 'Женщина'),
    ]
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default=MAN, )

    VERY_LOW = 'VL'
    LOW = 'L'
    AVERAGE = 'A'
    HIGH = 'H'
    VERY_HIGH = 'VH'
    PHYSICAL_ACTIVITY_CHOICES = [
        (VERY_LOW, 'Очень низкая физическая активность'),
        (LOW, 'Низкая физическая активность'),
        (AVERAGE, 'Средняя физическая активность'),
        (HIGH, 'Высокая физическая активность'),
        (VERY_HIGH, 'Очень высокая физическая активность'),
    ]
    physical_activity = models.CharField(max_length=9, choices=PHYSICAL_ACTIVITY_CHOICES, default=VERY_LOW, )

    LOSE_WEIGHT = 'LWeight'
    MAINTAIN_WEIGHT = 'MWeight'
    GAIN_WEIGHT = 'GWeight'
    TARGET_CHOICES = [
        (LOSE_WEIGHT, 'Похудеть'),
        (MAINTAIN_WEIGHT, 'Поддерживать вес'),
        (GAIN_WEIGHT, 'Набрать вес'),
    ]
    target = models.CharField(max_length=15, choices=TARGET_CHOICES, default=LOSE_WEIGHT, )
    objects = models.Manager()


class Product(models.Model):
    title = models.CharField(verbose_name='Название продукта', max_length=20, blank=True)
    proteins = models.FloatField(verbose_name='Белки', blank=True)
    fats = models.FloatField(verbose_name='Жиры', blank=True)
    carbohydrates = models.FloatField(verbose_name='Углеводы', blank=True)
    calories = models.FloatField(verbose_name='Калории', blank=True)
    objects = models.Manager()
