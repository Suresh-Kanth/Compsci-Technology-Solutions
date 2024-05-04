from django.db import models
from river.models.fields.state import StateField

#class MyModel(models.Model):


# Create your models here.
class Employee(models.Model):
    my_state_field = StateField()
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.EmailField()
    dob = models.DateField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    Aadhar_number = models.BigIntegerField()
    pan_number = models.CharField(max_length=10)
    
    def __str__(self):
        return self.firstname
    def natural_key(self):
        return self.Aadhar_number
