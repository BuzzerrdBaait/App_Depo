from django import forms
from .models import UserBook

from django.contrib.auth import get_user_model



class SavePageForm(forms.Form):

    def __init__(self, user, *args, **kwargs):

        super(SavePageForm, self).__init__(*args, **kwargs)

        self.fields['user_book'].queryset = UserBook.objects.filter(user=user)



    user_book = forms.ModelChoiceField(queryset=UserBook.objects.none(), empty_label=None, label="Select User Book")



class UserBookForm(forms.ModelForm):

    class Meta:

        model = UserBook

        fields = ['title']

class DeleteUserBookForm(forms.Form):

    def __init__(self, user, *args, **kwargs):

        super(DeleteUserBookForm, self).__init__(*args, **kwargs)

        self.fields['user_book'].queryset = UserBook.objects.filter(user=user)


    user_book = forms.ModelChoiceField(queryset=UserBook.objects.none(), empty_label=None, label="Select User Book")

class DeleteUserBookPageForm(forms.Form):

    user_book_page_id = forms.IntegerField(widget=forms.HiddenInput())


from .models import DefaultUserProfilePicture
    
from django import forms



class UserProfilePicChangeForm(forms.Form):

    user_pic = forms.ImageField(label='Upload a new profile picture', required=False)