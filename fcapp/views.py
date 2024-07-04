
from django.views.generic import ListView, DetailView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.views import View 
from .models import Deck, Card,WebImgs, Contact,Note
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import DeckForm, CardForm, DeleteCardForm, DeleteDeckForm,NoteForm
from collections import OrderedDict
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.contrib import messages

from django.urls import reverse


User = get_user_model()



def flashcards_home(request):

    """_____I imported OrderedDict and created an instance of a dictionary of the Deck.Category choices
    _____It sorts by the id # so I had to call lambda function and key[1] is used because the keywords 
    _____are in that column. So basically this is how to sort your items by the category choices defined
    _____in the model's category dictionary.

    """

    user_decks = Deck.objects.all()

    public_decks_by_category = {}

    category_choices_dict = dict(Deck.CATEGORY_CHOICES)

    sorted_categories = OrderedDict(sorted(category_choices_dict.items(), key=lambda key: key[1]))

    for category in sorted_categories.keys():

        public_decks_by_category[category] = Deck.objects.filter(public=True, category=category).order_by('category')


    return render(request, 'flashcards_home.html', {

        'user_decks': user_decks,

        'public_decks_by_category': public_decks_by_category,

    })


def user_profile_view(request, user_pk):

    user = get_object_or_404(User, pk=user_pk)

    user_decks = Deck.objects.filter(user=user)



    if request.method == 'POST':

        for deck in user_decks:

            public_checkbox_name = f'public_{deck.id}'

            if public_checkbox_name in request.POST:

                deck.public = True

            else:

                deck.public = False

            deck.save()

    




    return render(request, 'flashcards_user_profile.html', {'user_decks': user_decks, 'user':user})


@login_required

def create_deck(request):

    """
    Imported this Deck Form so users can have a view to create new decks
    """

    if request.method == 'POST':
        

            user = request.user

            user_decks_count = Deck.objects.filter(user=user).count()


            if user.is_verified == 'N' and user_decks_count >= 5:

                print('MAX LIMIT REACHED FOR UNAUTH USER')

                return redirect('home')


            if user.is_verified == 'Y' and user_decks_count >= 20:

                print("MAX LIMIT REACHED FOR AUTH USER")

                return redirect('fcapp:user_profile', user_pk=request.user.pk)



            form = DeckForm(request.POST)

            if form.is_valid():

                deck = form.save(commit=False)

                deck.user = request.user

                deck.save()

            return redirect('fcapp:user_profile', user_pk=request.user.pk)

    else:

        form = DeckForm()

    return render(request, 'create_deck.html', {'form': form})



####################################

@login_required

def add_notes(request, deck_id):

    deck = get_object_or_404(Deck, id=deck_id)



    # Check if the user is the owner of the deck

    if request.user == deck.user:

        if request.method == 'POST':

            form = NoteForm(request.POST)

            if form.is_valid():

                print("form is valid")

                notes = form.cleaned_data['note']

                Note.objects.create(deck=deck,user=request.user, note=notes)

                messages.success(request, 'Notes added successfully!')

                return redirect('fcapp:view_deck', deck_id=deck.id)

        else:

            form = NoteForm()



        return render(request, 'add_notes.html', {'form': form, 'deck': deck})
    
    else:

        messages.error(request, 'You do not have permission to add notes to this deck.')

        return redirect('view_deck', deck_id=deck.id)

##################################

def view_deck(request, deck_id):

    deck = get_object_or_404(Deck, id=deck_id)

    #will need this for production for fix images' paths

    cloudfront_url="https://d17usxoyp786nd.cloudfront.net/"

    images=WebImgs.objects.all()

    flip_button=images[1]

    left=images[0]

    right=images[2]

    flashcard=images[3]

    back=images[4]

    notes = Note.objects.filter(deck=deck)

    cards = Card.objects.filter(deck=deck)



    if request.method == 'POST':

        delete_card_form = DeleteCardForm(request.POST)

        if delete_card_form.is_valid():

            card_id = delete_card_form.cleaned_data['card_id']

            card_to_delete = get_object_or_404(Card, id=card_id, deck=deck)

            card_to_delete.delete()


        return redirect('view_deck', deck_id=deck.id)

    else:

        delete_card_form = DeleteCardForm()



    return render(request, 'view_deck.html', {'deck': deck, 'cards': cards, 'delete_card_form': delete_card_form, 'flip_button':flip_button, 'left':left,'right': right,'flashcard':flashcard, 'back':back, 'notes':notes})

@login_required

def create_card(request, deck_id):

    deck = Deck.objects.get(id=deck_id)

    if request.method == 'POST':

        user = request.user


        user_card_count = Card.objects.filter(deck__user=user).count()


        if user.is_verified == 'N' and user_card_count >= 250:

                return redirect('flashcards_home')



        if user.is_verified == 'Y' and user_card_count >= 2000:


                return redirect('fcapp:user_profile', user_pk=request.user.pk)
        

        form = CardForm(request.POST)

        if form.is_valid():

            card = form.save(commit=False)

            card.deck = deck

            card.save()

            return redirect('fcapp:view_deck', deck_id=deck.id)

    else:

        form = CardForm()

    return render(request, 'create_card.html', {'form': form, 'deck': deck})



#####################  EDIT CARDS, NOTES, AND DECK ##################


@login_required

def edit_card(request, card_id):

       card = get_object_or_404(Card, id=card_id, deck__user=request.user)

       if request.method == 'POST':

           form = CardForm(request.POST, instance=card)

           if form.is_valid():

               form.save()

               return redirect('view_deck', deck_id=card.deck.id)

       else:

           form = CardForm(instance=card)

       return render(request, 'edit_card.html', {'form': form, 'card': card})



@login_required

def edit_note(request, note_id):

       note = get_object_or_404(Note, id=note_id, user=request.user)

       if request.method == 'POST':

           form = NoteForm(request.POST, instance=note)

           if form.is_valid():

               form.save()

               return redirect('fcapp:view_deck', deck_id=note.deck.id)

       else:

           form = NoteForm(instance=note)

       return render(request, 'edit_note.html', {'form': form, 'note': note})




def edit_deck(request, deck_id):

    deck = get_object_or_404(Deck, id=deck_id)



    if request.method == 'POST':

            form = DeckForm(request.POST, instance=deck)

            delete_form = DeleteDeckForm(request.POST)



            if delete_form.is_valid():

                deck.delete()

                return redirect('fcapp:user_profile', user_pk=request.user.pk)



            if form.is_valid():

                deck_instance = form.save(commit=False)

                deck_instance.public = request.POST.get('public', False) == 'on'

                deck_instance.save()

                return redirect('fcapp:view_deck', deck_id=deck_id)

    else:

            form = DeckForm(instance=deck)

            delete_form = DeleteDeckForm(initial={'deck_id': deck_id})



    return render(request, 'edit_deck.html', {'form': form, 'delete_deck_form': delete_form, 'deck': deck})


def about_us(request):

    print("about us triggered")

    return render(request, 'fcapp:about_us.html')


def clep_resources(request):

    print("clep_resources")

    return render(request, 'fcapp:clep_resources.html')








