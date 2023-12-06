from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *


class UserView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        detail = [{"name": detail.name, "email": detail.email, "password": detail.password,
                   "birth_date": detail.birth_date, "height": detail.height, "weight": detail.weight,
                   "gender": detail.gender, "physical_activity": detail.physical_activity,
                   "target": detail.target}
                  for detail in User.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class ProductView(APIView):
    serializer_class = ProductSerializer

    def get(self, request):
        detail = [{"title": detail.title, "proteins": detail.proteins, "fats": detail.fats,
                   "carbohydrates": detail.carbohydrates, "calories": detail.calories}
                  for detail in Product.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
