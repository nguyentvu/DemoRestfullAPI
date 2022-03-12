from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(prefix='categories', viewset=views.CategoryViewset, basename='category')


urlpatterns = [
   path('', include(router.urls))
]