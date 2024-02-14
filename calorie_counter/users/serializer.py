from rest_framework import serializers

from .models import User, Product, Dish


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'birth_date', 'height', 'weight', 'gender', 'physical_activity',
                  'target']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'proteins', 'fats', 'carbohydrates', 'calories']


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'title', 'proteins', 'fats', 'carbohydrates', 'calories']
