from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from .views import UserViewSet, RestaurantViewSet, MenuViewSet, ReviewViewSet, ReservationViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('user', UserViewSet)
routers.register('restaurant', RestaurantViewSet)
routers.register('menu', MenuViewSet)
routers.register('review', ReviewViewSet)
routers.register('reservation', ReservationViewSet)
# routers.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(routers.urls)),
    path('rest-auth/', include('rest_auth.urls')),
]
