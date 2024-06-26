from django.urls import path, include


from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views

app_name='home_page'

urlpatterns = [
     
    path('', views.home, name='home'),

    
]




