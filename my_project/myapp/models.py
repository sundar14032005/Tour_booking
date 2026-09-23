from django.db import models
from django.contrib.auth.models import User

class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    available_seats = models.IntegerField()
    start_date = models.DateField()

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    seats = models.IntegerField()