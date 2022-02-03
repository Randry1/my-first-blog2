from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    """index catalog book"""
    return HttpResponse('<h1> Главная страница мир книг </h1>')
