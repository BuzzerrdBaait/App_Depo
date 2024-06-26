from django.urls import path, include

from . import views

app_name='profile_management'

urlpatterns=[

     path('user_profile/', views.user_profile, name='User_Profile'),

     path('login/', views.login_the_user, name='login'),

     path('register/', views.registration, name='register'),
]

