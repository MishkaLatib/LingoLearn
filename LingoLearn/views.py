from django.http import HttpRequest, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import random
import request
from django import forms
from .models import Category
from .models import User
from .models import Item
from .models import Points
from django.views import generic
from django.views.generic import View, FormView
from .forms import UserForm
from django.forms import ModelChoiceField
from django.contrib.auth import user_logged_in
from django.contrib.auth import authenticate, login
import getpass

def WelcomePage(request):
    return render(request, 'LingoLearn/WelcomePage.html')

class CategoriesPage(generic.ListView):
    template_name = 'LingoLearn/CategoriesPage.html'
    context_object_name = "categories"
    def get_queryset(self):
        return Category.objects.all()

class item_list(generic.ListView):
    template_name = 'LingoLearn/items.html'
    context_object_name = "items"
    def get_queryset(self):

        i = Item.objects.filter(category_id=self.kwargs['category_id'])
        print(i)
        return i

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
                    return redirect('WelcomePage')

        return render(request, self.template_name, {'form': form})


class ProfileView(generic.ListView):
    template_name = 'LingoLearn/ProfilePage.html'
    context_object_name = "points"

    def get_queryset(self):
        p = Points.objects.all()
        points = p[:4]
        return points


#Lingo Practise Game related Views

class GameCategoriesPage(generic.ListView):
    template_name = 'LingoLearn/GameCategoriesPage.html'
    context_object_name = "categories"
    def get_queryset(self):
        return Category.objects.all()


class GamePlay(generic.ListView):
    template_name = 'LingoLearn/GamePlay.html'
    context_object_name = "content"

    def __init__(self, **kwargs):
        super(GamePlay, self).__init__(**kwargs)
        self.POST = None
        self.GET = None


    def get_queryset(self):
        items = list(Item.objects.filter(category_id=self.kwargs['category_id']))
        random.shuffle(items)
        content = items[:5]
        possible_answers =list(content)
        random.shuffle(possible_answers)
        answer = possible_answers[0]
        #self.request.session['answer'] = "hfdkjfnhdkujnf"
        #self.request.session.save()
        content.append(answer)
        return content


def GainPoints(request):
    if request == 'POST':
        pointup = request.POST.get('pointup')
        p = Points.objects

        post = Points(user=request.user, points=points+pointup, )
        post.save()

