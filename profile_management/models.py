from django.db import models

""" USER_PROFILE IMPORTS"""
from django.contrib.auth.models import AbstractUser
import secrets
import string
"""_.-._.-._.-._"""

class User_Profile(AbstractUser):
    
    """  ALTERING THE DJANGO BASE USER MODEL.  
    """
    email=models.CharField(max_length=40, blank=True, null=True, unique=True)

    ilovecookbooks_profile_pic=models.ImageField(upload_to='ilovecookbooks_profile_images',default="none")

    authentication_key= models.CharField(max_length=50, unique=True)

    is_verified = models.CharField(max_length=1, default='N')

    authentication_link= models.CharField(max_length=50, blank=True, null=True)
    
    def generate_unique_link(self):
        
        """  MAKES THE LINK TO COPY AND PASTE YOUR AUTHENTICATION KEY
        """
        
        link = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range (30))

        # The next few lines replace characters that would make a link fail to generate properly.

        link = link.replace('\\', str(secrets.randbelow(1000)))

        link = link.replace('/', str(secrets.randbelow(1000)))

        link = link.replace('"', str(secrets.randbelow(1000)))

        link = link.replace("'", str(secrets.randbelow(1000)))


    def save(self, *args, **kwargs):
        
        """  MAKES THE AUTHENTICATION KEY UPON USER CREATION .
             
             CALLS generate_unique_link

             also any other things we want to add upon user creation.
        """
        
        if not self.authentication_key:
            
            self.authentication_key = ''.join(secrets.choice(string.ascii_letters +string.digits + string.punctuation) for _ in range(30))
     
        if not self.authentication_link:
            
            self.authentication_link = self.generate_unique_link()

        super().save(*args,**kwargs)
