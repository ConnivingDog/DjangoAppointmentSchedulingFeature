from django.shortcuts import render
from django.views import generic
from .models import Client, Appointment
from django.template import loader

class IndexView(generic.ListView):
    model = Client
    template_name = 'appointment/index.html'