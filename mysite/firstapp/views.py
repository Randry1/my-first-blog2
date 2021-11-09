from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    content = '<h1>Главная</h1>'
    content += '<a href="/firstapp/about/" class="btn btn-info">About</a><br>'
    content += '<a href="/firstapp/contact/" class="btn btn-info">Contact</a><br>'
    content += '<a href="/firstapp/products/2/" class="btn btn-info">Products 2</a><br>'
    content += '<a href="/firstapp/users/2/Maria/" class="btn btn-info">Users</a><br>'
    content += '<a href="/firstapp/blanks/1/Maria/89089462235/" class="btn btn-info">Бланк 1</a><br>'
    return HttpResponse(content)

def about(request):
    '''Пример реализации обработки запроса пользователя
    и строки запроса'''
    return HttpResponse('<h1> О нас</h1>')

def contact(request):
    ''' Второй пример использования запроса пользлавтеля'''
    return HttpResponse('<h2> Контакты с нами</h2>')

def products(request, productid):
    '''Функция для изучения получения данных из запроса url адреса
    http://127.0.0.1:8000/firstapp/produsts/2/'''
    return HttpResponse("<h1>Продукт № {0}".format(productid))

def users(request, id, name):
    '''Функйия получения данныйх из URL запроса
    http://127.0.0.1:8000/firstapp/users/2/Maria/'''
    return HttpResponse("<h1>Привет {0} ваш id:{1}</h1>".format(name,id))

def blanks(request, blankid, name, phone):
    '''Моя функция для того чтобы пронять правильно ли получил как вытащить переменные из URL запроса
    http://127.0.0.1:8000/firstapp/blanks/1/Maria/89089462235/'''
    page ="<h1>Номер бланка {0}, заполнен на {1}, телефон {2} </h1>".format(blankid, name, phone)
    return HttpResponse(page)