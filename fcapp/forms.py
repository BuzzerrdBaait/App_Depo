from django import forms

from .models import *



class DeckForm(forms.ModelForm):

    class Meta:

        model = Deck

        fields = ['title','description', 'category','public']

        widgets = {

            'public': forms.CheckboxInput(), 

        }


class NoteForm(forms.ModelForm):

        class Meta:

            model = Note

            fields = ['note']

            widgets={
                'note':
                forms.Textarea(attrs={'rows':15})
            }

class CardForm(forms.ModelForm):

    class Meta:

        model = Card

        fields = ['question', 'answer']


class DeleteDeckForm(forms.Form):

    deck_id = forms.IntegerField(widget=forms.HiddenInput)

class DeleteCardForm(forms.Form):

    card_id = forms.IntegerField(widget=forms.HiddenInput)



    
