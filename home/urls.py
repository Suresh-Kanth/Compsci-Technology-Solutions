from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls import url, include
from home.views import approve_Employee
urlpatterns = [
    path('',views.form,name="home"),
    url(r'^approve_Employee/(?P<Employee_id>\d+)/(?P<next_state_id>\d+)/$', approve_Employee, name='approve_Employee'),
]
