from PIL import Image

import PIL.Image

from io import BytesIO

from django.db import models

from django.core.files.storage import default_storage

from django.core.files.base import ContentFile

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

from django.db import models

from django.db.models.signals import post_save

from django.dispatch import receiver


User=get_user_model()



class Book(models.Model):

    title = models.CharField(max_length=200)

    year = models.PositiveSmallIntegerField()

    cover_photo = models.ImageField(upload_to='book_covers/')

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        self.compress_and_optimize_image(self.cover_photo)

    def compress_and_optimize_image(self, image_field):
        print("compress triggered on--->",image_field)

        img = Image.open(image_field)

        buffer = BytesIO()

        img.save(buffer, format='JPEG', quality=20, optimize=True)

        buffer.seek(0)

        file_name = image_field.name

        file_content = ContentFile(buffer.read())

        default_storage.save(file_name, file_content)

        # Optionally, delete the local file if needed

        # image_field.delete(save=False)

        # Update the image field with the S3 path

        image_field.name = file_name

    def __str__(self):

        return self.title

class BookPage(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pages')

    keywords = models.CharField(max_length=5000, blank=True)

    page_photo = models.ImageField(upload_to='book_pages/')
    
    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        self.compress_and_optimize_image(self.page_photo)

    def compress_and_optimize_image(self, image_field):

        print("compress triggered on--->", image_field)

        img = Image.open(image_field)

        buffer = BytesIO()

        img.save(buffer, format='JPEG', quality=20, optimize=True)

        buffer.seek(0)

        file_name = image_field.name

        file_content = ContentFile(buffer.read())

        default_storage.save(file_name, file_content)

        image_field.name = file_name

        def __str__(self):

            return f"Page {self.pk} of {self.book.title}"
        



class Post(models.Model):

    title = models.CharField(max_length=255)

    video_file = models.FileField(upload_to='blog_videos/')

    thumbnail = models.ImageField(upload_to='thumbnails/')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    body = models.TextField()

    date = models.DateField()

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        self.compress_and_optimize_image(self.thumbnail)

    def compress_and_optimize_image(self, image_field):

        img = Image.open(image_field)

        buffer = BytesIO()

        img.save(buffer, format='JPEG', quality=20, optimize=True)

        buffer.seek(0)

        file_name=img.name

        file_content = ContentFile(buffer.read())

        default_storage.save(file_name, file_content)

        image_field.name = file_name

    def __str__(self):

        return self.title + '|' + str(self.author)


class WebImgs(models.Model):

    title = models.CharField(max_length=25)

    thumbnail = models.ImageField(upload_to='web_imgs/')

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        self.compress_and_optimize_image(self.thumbnail)

    def compress_and_optimize_image(self, image_field):

        img = Image.open(image_field)

        img.save(image_field.path, format='JPEG', quality=20, optimize=True)



class UserBook(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    pages = models.ManyToManyField(BookPage, through='UserBookPage')

    def save(self, *args, **kwargs):

        if not self.title:

            self.title = f"{self.user.username}_{self.title}"

        super(UserBook, self).save(*args, **kwargs)

    def __str__(self):

        return self.title


class UserBookPage(models.Model):

    user_book = models.ForeignKey(UserBook, on_delete=models.CASCADE)

    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)

    order = models.PositiveIntegerField(default=000)  # An order field to specify the page order within the book

    def save(self, *args, **kwargs):

        if not self.order:

            existing_pages = UserBookPage.objects.filter(user_book=self.user_book)

            self.order = existing_pages.count() + 1

        super(UserBookPage, self).save(*args, **kwargs)


class DefaultUserProfilePicture(models.Model):

    name = models.CharField(max_length=255, unique=True)

    image = models.ImageField(upload_to='flashcards_profile_imgs/')

    def __str__(self):

        return self.name
    























