from django.shortcuts import get_object_or_404, redirect, render
from core.models import Room, Booking
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }

    return render(request, template_name="booking/room_list.html", context=context)


@login_required
def book_room(request, room_id):

    room = get_object_or_404(Room, id=room_id)

    if request.method == "POST":
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")
        
        booking = Booking.objects.create(
            user = request.user,
            room=room,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('booking-details', pk=booking.id)
    else:
        return render(request, template_name="booking/booking_form.html", context={"room": room})
    
def booking_details(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
        context = {
            "booking": booking
        }
        return render(request, template_name="booking/booking_details.html", context=context)
    except Booking.DoesNotExist:
        return HttpResponse(
            "this booking does not exist",
            status = 404
        )