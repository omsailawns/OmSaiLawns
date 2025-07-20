from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),  # This is the fix
    path('api/booked-dates/', views.booked_dates, name='booked_dates'),
]
