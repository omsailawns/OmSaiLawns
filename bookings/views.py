from django.http import JsonResponse
from django.shortcuts import render
from .models import Booking

def homepage(request):
    return render(request, 'index.html')

def booked_dates(request):
    bookings = Booking.objects.all()
    dates = {}
    for booking in bookings:
        key = booking.event_date.strftime("%Y-%m")
        day = str(booking.event_date.day)
        dates.setdefault(key, []).append(day)
    return JsonResponse(dates)
