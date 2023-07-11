from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

from .models import User, Restaurant, Menu, Review, Reservation
from .serializers import UserSerializer, RestaurantSerializer, MenuSerializer, ReviewSerializer, ReservationSerializer

# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods=['get'])
    def user_reviews(self, request, pk):
        user = self.get_object()
        reviews = user.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
# class RestaurantViewSet(viewsets.ModelViewSet):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer
    
#     @action(detail=True, methods=['get'])
#     def restaurant_reviews(self, request, pk):
#         restaurant = self.get_object()
#         reviews = restaurant.review_set.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    # @action(detail=True, methods=['get'])
    # def restaurant_reviews(self, request, pk):
    #     reviews = Review.objects.get(restaurant=pk)
    #     serializer = ReviewSerializer(reviews, many=True)
    #     return Response(serializer.data)
    
    
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    filter_backends = [SearchFilter]
    search_fields = ['restaurant__name']    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    