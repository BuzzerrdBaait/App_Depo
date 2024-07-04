from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.urls import path

from .views import *

app_name = "fcapp"

urlpatterns = [
     
    path('flashcards/', views.flashcards_home, name='flashcards_home'),

    path('flashcards/create_deck/', views.create_deck, name='create_deck'),

    path('flashcards/view/<int:deck_id>/', views.view_deck, name='view_deck'),

    path('flashcards/add_notes/<int:deck_id>/', views.add_notes, name='add_notes'),

    path('flashcards/<int:deck_id>/edit/', views.edit_deck, name='edit_deck'),

    path('flashcards/create_card/<int:deck_id>/', views.create_card, name='create_card'),

    path('flashcards/edit_card/<int:card_id>/', views.edit_card, name='edit_card'),

    path('flashcards/edit_note/<int:note_id>/', views.edit_note, name='edit_note'),

    path('flashcards/profile/<int:user_pk>/', views.user_profile_view, name='user_profile'),

    path('flashcards/about', views.about_us, name='about_us'),

    path('flashcards/clep', views.clep_resources, name='clep'),

    path('flashcards/logout', auth_views.LogoutView.as_view(), name='logout'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





