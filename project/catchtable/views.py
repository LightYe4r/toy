from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import User, Restaurant, Menu, Review, Reservation, UserManager
from .serializers import UserSerializer, RestaurantSerializer, MenuSerializer, ReviewSerializer, ReservationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods=['get'])
    def user_reviews(self, request, pk):
        user = self.get_object()
        reviews = user.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def user_reservations(self, request, pk):
        user = self.get_object()
        reservations = user.reservation_set.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    @action(detail=True, methods=['get'])
    def restaurant_reviews(self, request, pk):
        restaurant = self.get_object()
        reviews = restaurant.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def restaurant_menus(self, request, pk):
        restaurant = self.get_object()
        menus = restaurant.menu_set.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
    
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
     
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    