from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    open_hours = models.CharField(max_length=100)
    location_x = models.FloatField() #경도, longitude
    location_y = models.FloatField() #위도, latitude
    address = models.CharField(max_length=50, default='')
    
class Menu(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Review(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    score = models.IntegerField()

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    party_count = models.IntegerField()
    requiurement = models.TextField()
    status = models.CharField(max_length=30)