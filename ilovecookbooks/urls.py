
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



from django.urls import path, include
from . import views
from .views import blogview, videopage, BookDetailView,UserProfileView
from django.conf.urls import *
from django.urls import path 
from django.contrib import admin



app_name= "ilovecookbooks"

urlpatterns = [
    path("ilovecookbooks", views.Main, name="Main"),

    path("ilovecookbooks2", views.Main, name="Home"),

    path('ilovecookbooks/foodblog/', blogview.as_view(), name="foodblog"),

    path('ilovecookbooks/details/<int:pk>', videopage.as_view(), name='details'),

    path('ilovecookbooks/book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    
    path('ilovecookbooks/links/', views.link_view, name='links'),

    path('ilovecookbooks/base/', views.base, name='base'),

    path('ilovecookbooks/search/', views.search_results, name='search_results'),


    path('ilovecookbooks/profile/<int:pk>/', views.UserProfileView, name='user_profile'),

    path('ilovecookbooks/user_books/<int:user_book_id>/', views.user_book_pages, name='user_book_pages'),

    path('ilovecookbooks/page/<int:page_id>/book/<int:book_id>/', views.page_view, name='page_view'),

    path('ilovecookbooks/default_profile_images/<int:pk>/', views.default_profile_images, name='default_profile_images'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
