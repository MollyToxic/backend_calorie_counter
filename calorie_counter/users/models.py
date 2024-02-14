from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

# Модель пользователя (расширение модели пользователей)
class User(AbstractUser):
    birth_date = models.DateField(verbose_name='Дата рождения', default=date(2000, 1, 1))
    height = models.IntegerField(verbose_name='Рост', default=160)
    weight = models.IntegerField(verbose_name='Вес', default=50)

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

    # objects = models.Manager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email', 'birth_date']

# Модель продуктов
class Product(models.Model):
    title = models.CharField(verbose_name='Название продукта', max_length=20, blank=True)
    proteins = models.FloatField(verbose_name='Белки', blank=True)
    fats = models.FloatField(verbose_name='Жиры', blank=True)
    carbohydrates = models.FloatField(verbose_name='Углеводы', blank=True)
    calories = models.FloatField(verbose_name='Калории', blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']

# Модель блюд
class Dish(models.Model):
    title = models.CharField(verbose_name='Название блюда', max_length=20, blank=True)
    proteins = models.FloatField(verbose_name='Белки', blank=True)
    fats = models.FloatField(verbose_name='Жиры', blank=True)
    carbohydrates = models.FloatField(verbose_name='Углеводы', blank=True)
    calories = models.FloatField(verbose_name='Калории', blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['title']

# Модель рецептов (для связи продуктов и блюд)
class Recipe(models.Model):
    productID = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт', null=True)
    grams = models.FloatField(verbose_name='Граммовки этого продукта', blank=True)
    dishID = models.ForeignKey('Dish', on_delete=models.CASCADE, verbose_name='Блюдо', null=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['dishID']
