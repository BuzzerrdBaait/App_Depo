from django.urls import path, include


from django.contrib.auth import views as auth_views
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name='home_page'

urlpatterns = [
     
    path('', views.home, name='home'),

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





