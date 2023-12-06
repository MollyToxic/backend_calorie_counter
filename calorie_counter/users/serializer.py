from rest_framework import serializers
from .models import User, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'birth_date', 'height', 'weight', 'gender', 'physical_activity',
                  'target']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'proteins', 'fats', 'carbohydrates', 'calories']
