from django.contrib import admin
from .models import User_Profile

from django.utils.html import format_html
from .models import User_Profile
# Register your models here.

@admin.register(User_Profile)

class User_Profile_Info(admin.ModelAdmin):

     list_display=('username','email','ilovecookbooks_profile_pic_thumbnail','is_verified')

     def ilovecookbooks_profile_pic_thumbnail(self, obj):
        if obj.ilovecookbooks_profile_pic:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(obj.ilovecookbooks_profile_pic.url))
        else:
            return "No Image"

     ilovecookbooks_profile_pic_thumbnail.short_description = 'Profile Picture'
     ilovecookbooks_profile_pic_thumbnail.allow_tags = True

