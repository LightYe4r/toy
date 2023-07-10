import rest_framework.serializers as serializers
from .models import User, Restaurant, Menu, Review, Reservation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
        depth = 1
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'