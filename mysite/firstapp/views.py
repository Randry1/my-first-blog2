from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Главная</h1>')

def about(request):
    '''Пример реализации обработки запроса пользователя
    и строки запроса'''
    return HttpResponse('<h1> О нас</h1>')

def contact(request):
    ''' Второй пример использования запроса пользлавтеля'''
    return HttpResponse('<h2> Контакты с нами</h2>')