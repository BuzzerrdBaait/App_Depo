
from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

# from .forms import *
from .models import logo_images,misc_images

import os


User = get_user_model()

def home(request):

     misc_imgs= misc_images.objects.all()

     logos= logo_images.objects.all()

     ilovecookbooks_logo=logos[0]

     flashcards=logos[1]


     greeting="The daily message is: 'Love conquers all!'"

     return render(request, 'home.html',{

          'greeting': greeting,
          'misc_imgs':misc_imgs,
          'ilovecookbooks':ilovecookbooks_logo,
          'flashcards' : flashcards,
          })


#<img src="{{ rocket.image.url}}" alt="rocket">