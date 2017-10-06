from django.shortcuts import render, redirect
import random
from .models import Category
from .models import Item
from .models import Badges
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import authenticate, login

#function to call LingoLearn Welcome page
def WelcomePage(request):
    return render(request, 'LingoLearn/WelcomePage.html')


#Displays Categories that can be selected to begin in Learning mode.
## Category links to set of images under the category, linked in the database

class CategoriesPage(generic.ListView):
    template_name = 'LingoLearn/CategoriesPage.html'
    context_object_name = "categories"
    def get_queryset(self):
        return Category.objects.all()


#Displays all images pulled from database with Foreign key
# matching that of the selected Category from the CategoriesPage

class item_list(generic.ListView):
    template_name = 'LingoLearn/items.html'
    context_object_name = "items"
    def get_queryset(self):

        i = Item.objects.filter(category_id=self.kwargs['category_id'])
        return i


#User form to insert Name, Surname, Username and Password in order to register an account with LingoLearn
#This can be monitored via the admin site
#makes use of Django admin imports

class UserFormView(View):
    form_class = UserForm
    template_name = 'LingoLearn/reg_form.html'

    #display form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.set_password(password)
            user.save()

            #returns User object if creds match database
            user= authenticate(username=username, password=password)
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('LingoLearn:WelcomePage')

        return render(request, self.template_name, {'form': form})



#Personalised Welcome page, indicating Login

class ProfileView(generic.ListView):
    template_name = 'LingoLearn/ProfilePage.html'
    context_object_name = "badges"

    def get_queryset(self):
        badges = Badges.objects.all()
        return badges


#Lingo Practise Game related Views. Links to items page

class GameCategoriesPage(generic.ListView):
    template_name = 'LingoLearn/GameCategoriesPage.html'
    context_object_name = "categories"
    def get_queryset(self):
        return Category.objects.all()


#Class to load game depending on selected category. 5 images are shown at once.

class GamePlay(generic.ListView):
    template_name = 'LingoLearn/GamePlay.html'
    context_object_name = "content"

    def __init__(self, **kwargs):
        super(GamePlay, self).__init__(**kwargs)
        self.POST = None
        self.GET = None

    # 6 elements are passed through as a list as the 6th is the answer, and therefore a dupllicate of another one of the 5. This is for running answer checks later

    def get_queryset(self):
        items = list(Item.objects.filter(category_id=self.kwargs['category_id']))
        random.shuffle(items)
        content = items[:5]
        possible_answers =list(content)
        random.shuffle(possible_answers)
        answer = possible_answers[0]
        content.append(answer)
        return content


#currently unused. Intended to send score back to ProfilePage

score = None

def getScore(self, request, score):
    if score==None:
        score = 0
        return score
    else:
        return score

def GainPoints(self, request, score):
    score+=1
    return score

