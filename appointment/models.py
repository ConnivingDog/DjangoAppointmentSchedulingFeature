from django.db import models
from django.contrib import admin

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)

    def Client_Name(self):
        return self.first_name + ' ' + self.last_name

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    schedule = models.DateTimeField('appointment schedule')
