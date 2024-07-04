from django.contrib import admin

from .models import *

from django.utils.html import format_html


@admin.register(WebImgs)

class web_img_admin(admin.ModelAdmin):

    list_display=('title','image_thumbnail')

    def image_thumbnail(self,obj):
         if obj.image:
              
              return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(obj.image.url))
         else:
              return "No Image"
         
    
    image_thumbnail.short_description="Web assets"
    image_thumbnail.allow_tags= True





admin.site.register(Deck)

admin.site.register(Card)

admin.site.register(Note)
