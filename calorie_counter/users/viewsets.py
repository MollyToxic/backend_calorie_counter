from django.forms import model_to_dict
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import *
from .serializer import *


class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        us = User.objects.all().values()
        return Response({'users': list(us)})

    def post(self, request):
        new_us = User.objects.create(
            email=request.data['email'],
            username=request.data['username'],
            password=request.data['password'],
            birth_date=request.data['birth_date'],
            height=request.data['height'],
            weight=request.data['weight'],
            gender=request.data['gender'],
            physical_activity=request.data['physical_activity'],
        )
        return Response({'users': model_to_dict(new_us)})


class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DishAPIView(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
