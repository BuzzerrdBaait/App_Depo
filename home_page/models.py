from django.db import models


class misc_images(models.Model):
    
    name= models.CharField(max_length=50)

    image= models.ImageField(upload_to="misc")

class logo_images(models.Model):

    name= models.CharField(max_length=50)

    image=models.ImageField(upload_to="logo_images")