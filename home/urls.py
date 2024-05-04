from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls import url, include
urlpatterns = [
    path('',views.form,name="home"),
    url(r'^', include("river_admin.urls"))
]
