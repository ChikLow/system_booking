from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    class Level(models.TextChoices):
        STANDARD = "STD", "Standard"
        PREMIUM = "PRM", "Premium"
        VIP = "VIP", "VIP"

    number = models.IntegerField()
    location = models.TextField()
    level = models.CharField(max_length=3, choices=Level.choices)
    image = models.ImageField(upload_to='room_images', null=True, blank=True)

    LEVEL_PRICES = {
        Level.STANDARD: 500,
        Level.PREMIUM: 1000,
        Level.VIP: 2500,
    }

    LEVEL_CAPACITY = {
        Level.STANDARD: 2,
        Level.PREMIUM: 4,
        Level.VIP: 8,
    }

    @property
    def price(self):
        return self.LEVEL_PRICES.get(self.level, 0)

    @property
    def capacity(self):
        return self.LEVEL_CAPACITY.get(self.level, 0)

    def __str__(self):
        return f"Room #{self.number} - capacity {self.capacity} - price {self.price}$"

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.room}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["start_time"]