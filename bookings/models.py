from django.db import models

class Booking(models.Model):
    event_date = models.DateField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.event_date} - {self.name}"