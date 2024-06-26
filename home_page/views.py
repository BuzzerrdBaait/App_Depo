
from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.urls import reverse

# from .forms import *
from .models import *


User = get_user_model()

def home(request):

     greeting="The daily message is: 'Love conquers all!'"

     return render(request, 'home.html',{

          'greeting': greeting,})