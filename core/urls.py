from django.urls import path
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("room-list/", views.room_list, name="rooms-list"),
    path("book-room/", views.book_room, name="book-room"),
    path("booking-details/<int:pk>", views.booking_details, name="booking-details"),
]