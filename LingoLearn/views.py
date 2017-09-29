from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from .models import Item

def WelcomePage(request):
    return render(request, 'LingoLearn/WelcomePage.html')

def CategoriesPage(request):
    categories = Category.objects.all()
    cat = {'categories': categories}
    return render(request, 'LingoLearn/CategoriesPage.html', cat)

def item_list(request, category_id):
    i = Item.objects.filter(category_id = category_id)
    it = {'i' : i}
    return render(request, 'LingoLearn/items.html', it)

