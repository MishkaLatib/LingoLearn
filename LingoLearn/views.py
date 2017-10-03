from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Category
from .models import Item
from django.views import generic
from django.views.generic import View
from .forms import UserForm

def WelcomePage(request):
    return render(request, 'LingoLearn/WelcomePage.html')

class CategoriesPage(generic.ListView):
    template_name = 'LingoLearn/CategoriesPage.html'
    context_object_name = "categories"
    def get_queryset(self):
        return Category.objects.all()

#def CategoriesPage(request):
    #categories = Category.objects.all()
    #cat = {'categories': categories}
    #return render(request, 'LingoLearn/CategoriesPage.html', cat)

#class item_list(generic.ListView):
 #   template_name = 'LingoLearn/items.html'
  #  context_object_name = "items"
   # def get_queryset(self):
    #    return Item.objects.filter(category_id = )


def item_list(request, category_id):
    i = Item.objects.filter(category_id = category_id)
    it = {'items' : i}
    return render(request, 'LingoLearn/items.html', it)

class UserFormView(View):
    form_class = UserForm
    template_name = 'LingoLearn/reg_form.html'

    #display form
    def get(self, request):
        form = self.form_class

    def post(self, request):
        pass