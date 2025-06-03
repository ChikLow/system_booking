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

def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")

        try:
            room = room.objects.get(number=room_number)
        except ValueError:
            return HttpResponse(
                "Wrong value or room number",
                status = 400
            )
        except Room.DoesNotExist:
            return HttpResponse(
                "this room does not exist",
                status = 404
            )
        
        booking = Booking.objects.create(
            user = request.user,
            room=room,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('booking-details', pk=booking.id)
    else:
        return render(request, template_name="booking/booking_form.html")
    
def booking_details(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
        context = {
            "booking": booking
        },
        return render(request, template_name="booking/booking_details.html", context=context)
    except Booking.DoesNotExist:
        return HttpResponse(
            "this booking does not exist",
            status = 404
        )