from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from users.viewsets import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', UserAPIView.as_view()),
    path('api/v1/products/', ProductAPIView.as_view()),
    path('api/v1/dish/', DishAPIView.as_view()),
    path('api/v1/auth/', include('rest_framework.urls')),
]
