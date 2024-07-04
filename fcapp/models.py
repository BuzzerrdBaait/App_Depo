import secrets

import string

from django.contrib.auth.models import AbstractUser, Group, Permission

from django.db import models

from django.contrib.auth import get_user_model

User=get_user_model()




class Deck(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    description = models.TextField()  # Text field instead of ImageField

    public= models.BooleanField(default=False)

    CATEGORY_CHOICES=[

        ('Science','Science'),
        ('Technology','Technology'),
        ('Engineering','Engineering'),
        ('Mathematics','Mathematics'),
        ('History','History'),
        ('Literature','Literature'),
        ('Languages','Languages'),
        ('Arts','Arts'),
        ('Health and Medicine','Health & Medicine'),
        ('Programming','Programming'),
        ('Lifeskills','Lifeskills/Self Help'),
        ('CLEP', 'CLEP Exams'),
        ('Misc','Misc.'),
        
    ]

    category= models.CharField(max_length=25, default='Misc', choices=CATEGORY_CHOICES)



    def __str__(self):

        return self.title
    




from django.utils import timezone

from django.db.models.signals import pre_delete

from django.dispatch import receiver



class Note(models.Model):

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    note = models.TextField()

    date = models.DateTimeField(default=timezone.now())

    title = models.CharField(max_length=255, blank=True, null=True)



    def save(self, *args, **kwargs):

        if not self.pk:  # Only update on new note creation

            note_count_in_deck = Note.objects.filter(deck=self.deck).count() + 1

            self.title = f"Note {note_count_in_deck} of {self.deck.title}"

        super().save(*args, **kwargs)



    def __str__(self):

        return self.title



@receiver(pre_delete, sender=Note)

def update_note_titles_on_delete(sender, instance, **kwargs):

    remaining_notes = Note.objects.filter(deck=instance.deck).exclude(pk=instance.pk).order_by('pk')

    for index, note in enumerate(remaining_notes, start=1):

        note.title = f"Note {index} of {note.deck.title}"

        note.save()









class Card(models.Model):


    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    question = models.TextField()

    answer = models.TextField() 


    def __str__(self):

        return f"Card {self.pk} of {self.deck.title}"
    

class WebImgs(models.Model):

    title= models.CharField(max_length=32,blank=True)

    image= models.ImageField(upload_to='flashcards_web_imgs')

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)



class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    message = models.TextField()

    current_date = models.DateTimeField(auto_now_add=True)


