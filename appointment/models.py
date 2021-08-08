from django.db import models
from django.contrib import admin

class Client(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)

    def Client_Name(self):
        return self.firstname + ' ' + self.lastname

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    schedule = models.DateTimeField('appointment schedule')
