from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Employee
from django.contrib import messages

# Create your views here.
def form(request):
    if (request.method == 'POST'):
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        aadharnumber = request.POST.get('aadharnumber')
        phonenumber = request.POST.get('phoneNumber')
        pannumber = request.POST.get('pannumber')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        empoloyee = Employee(address=address,firstname=firstname,lastname=lastname,email=email,Aadhar_number=aadharnumber,phone_number=phonenumber,pan_number=pannumber,dob=dob)
        empoloyee.save()
        messages.success(request, "Profile details updated.")
    return render(request,'index.html')