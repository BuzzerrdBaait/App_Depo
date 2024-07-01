
from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.urls import reverse

from .forms import *
from .models import *


User = get_user_model()

def home(request):

     greeting="The daily message is: 'Love conquers all!'"

     return render(request, 'home.html',{

          'greeting': greeting,})

def user_profile(request):

     greeting="User Profile!"

     return render(request, 'user_profile.html',{

          '': greeting,})

def login_the_user(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('home_page:home')

        else:

            error_message = "Invalid credentials"

            return render(request, 'Error.html', {'error_message': error_message})

    else:

        return render(request, 'login.html')
    

def registration(request):

    """

    This creates a user model based on the User_Profile model which is the base User model extended.

    """

    if request.method == 'POST':

        form = Registration(request.POST)

        if form.is_valid():

            user_data = form.cleaned_data

            new_user = User_Profile.objects.create_user(

                username=user_data['username'],

                email=user_data['email'],

                password=user_data['password'],

            )

            try:

                registration_link = request.build_absolute_uri(

                    reverse('authenticate_user', args=[str(new_user.authentication_link)])

                )

                send_mail(

                    f"Welcome {new_user.username}",

                    f"Welcome to Flashcardzz!\n\n Here is how to get registered:\n\nBelow is your authentication key.\n\ncopy this:\n\n{new_user.authentication_key} \n\nClick the link below to complete your registration:\n\n{registration_link}",

                    "admin@ilovecookbooks.org",

                    [new_user.email],

                    fail_silently=False,

                )

            except:

                print("Sending an email failed")

            return render(request, 'login.html')

    else:

        form = Registration()

    return render(request, 'registration.html', {'form': form})
