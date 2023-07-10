from django.contrib import admin
from .models import User, Restaurant, Menu, Review, Reservation
# Register your models here.
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Review)
admin.site.register(Reservation)