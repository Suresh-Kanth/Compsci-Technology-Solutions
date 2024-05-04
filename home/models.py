from django.db import models
from river.models.fields.state import StateField
import uuid

# Create your models here.
class Employee(models.Model):
    no = models.CharField("Employee Number", max_length=50, default=uuid.uuid4, null=False, blank=False, editable=False,
                          unique=True)
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.EmailField()
    dob = models.DateField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    Aadhar_number = models.BigIntegerField()
    pan_number = models.CharField(max_length=10)
    my_state_field = StateField(editable=False)
    
    def natural_key(self):
        return self.no
    def __str__(self):
        return self.firstname
