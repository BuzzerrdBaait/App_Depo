from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# from .forms import *
from .models import *


User = get_user_model()

def experiment_room_1(request):

     greeting="Experimental Room 1"

     return render(request, 'experimental_room_1.html',{

          '': greeting,})

