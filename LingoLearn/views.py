from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template.backends import django

from .models import Category
from .models import Item
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import user_logged_in
from django.contrib.auth import authenticate, login

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


def ProfileView(request):
    return render(request, 'LingoLearn/ProfilePage.html')



#Lingo Practise Game related Views

class GameCategoriesPage(generic.ListView):
    template_name = 'LingoLearn/GameCategoriesPage.html'
    context_object_name = "categories"
    def get_queryset(self):
        return Category.objects.all()