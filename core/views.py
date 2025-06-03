from django.shortcuts import render
from core.models import Room, Booking
from django.http import HttpResponse

def index(request):
    context = {
        "render_string": "Hello, world!"
    }

    return render(request, template_name="booking/index.html", context=context)


def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }

    return render(request, template_name="booking/room_list.html", context=context)