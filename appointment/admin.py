from django.contrib import admin
from .models import Client, Appointment

admin.site.register(Appointment)
admin.site.register(Client)