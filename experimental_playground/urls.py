from django.urls import path
from . import views
app_name='experimental_playground'

urlpatterns=[

     path('X1', views.experiment_room_1,name='x1')
]