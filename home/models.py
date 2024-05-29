import uuid
from django.db import models
from river.models.fields.state import StateField
# Create your models here.
class Employee(models.Model):
    no = models.CharField("Employee Number",max_length=50, default=uuid.uuid4, null=False, blank=False, editable=False,unique=True)
    firstname = models.CharField("First Name", max_length=122, null=False, blank=False)
    lastname = models.CharField("Last Name", max_length=122, null=False, blank=False)
    email = models.EmailField("Email", null=False, blank=False)
    dob = models.DateField("Date of Birth", null=False, blank=False)
    phone_number = models.CharField("Phone Number", max_length=15, null=False, blank=False)
    address = models.TextField("Address", null=False, blank=False)
    Aadhar_number = models.BigIntegerField("Aadhar Number", null=False, blank=False)
    pan_number = models.CharField("PAN Number", max_length=10, null=False, blank=False)
    status = StateField(editable=False)
    
    def natural_key(self):
        return self.no
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
