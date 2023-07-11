from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, RestaurantViewSet, MenuViewSet, ReviewViewSet, ReservationViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('user', UserViewSet)
routers.register('restaurant', RestaurantViewSet)
# routers.register('restaurant/restaurant-reviews', RestaurantViewSet)
routers.register('menu', MenuViewSet)
routers.register('review', ReviewViewSet)
routers.register('reservation', ReservationViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]
