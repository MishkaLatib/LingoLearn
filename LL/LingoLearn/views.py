from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1> Welcome to LingoLearn!</h1>")