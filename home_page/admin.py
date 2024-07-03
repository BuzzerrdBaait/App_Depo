from django.contrib import admin
from django.utils.html import format_html


from .models import *

@admin.register(misc_images)

class misc_img_admin(admin.ModelAdmin):

     list_display=('name', 'image_preview')

     def image_preview(self, obj):

        if obj.image:

            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)

        return "No Image"
     
     image_preview.short_description = 'Image_Preview'
     image_preview.allow_tags=True

@admin.register(logo_images)

class logo_admin(admin.ModelAdmin):

    list_display=('name', 'image_preview')
    
    def image_preview(self, obj):

        if obj.image:

            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)

        return "No Image"
     
    image_preview.short_description = 'Image_Preview'
    image_preview.allow_tags=True


    