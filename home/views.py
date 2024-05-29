from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Employee
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from river.models import State
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

def approve_Employee(request, Employee_id, next_state_id=None):
    employee = get_object_or_404(Employee, pk=Employee_id)
    next_state = get_object_or_404(State, pk=next_state_id)

    try:
        employee.river.status.approve(as_user=request.user, next_state=next_state)
        return redirect(reverse('admin:home_employee_changelist'))
    except Exception as e:
        return HttpResponse(str(e))