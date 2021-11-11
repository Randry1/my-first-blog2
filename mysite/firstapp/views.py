from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# Create your views here.
def index(request):
    content = '<h1>Главная</h1>'
    content += '<a href="/firstapp/about/" class="btn btn-info">About</a><br>'
    content += '<a href="/firstapp/contact/" class="btn btn-info">Contact</a><br>'
    content += '<a href="/firstapp/detail/" class="btn btn-info">Detail перенаправление HttpResponsePermanentRedirect(\'/firstapp\')</a><br>'
    content += '<a href="/firstapp/products/2/" class="btn btn-info">Products 2</a><br>'
    content += '<a href="/firstapp/users/2/Maria/" class="btn btn-info">Users</a><br>'
    content += '<a href="/firstapp/blanks/1/Maria/89089462235/" class="btn btn-info">Бланк 1</a><br>'
    content += '<a href="/firstapp/mod_products/" class="btn btn-info">Бланк без номера</a><br>'
    content += '<a href="/firstapp/posts/2/edit/" class="btn btn-info">Пост edit с id</a><br>'
    content += '<a href="/firstapp/posts/2/Gleb/" class="btn btn-info">Пост edit с id и именем</a><br>'
    content += '<a href="/firstapp/posts/2/sdfsad/?pk=3&kategori=poni&othes=fdgsa" class="btn btn-info">Пост edit с id и именем + request.GET.get()</a><br>'
    return HttpResponse(content)

def about(request):
    '''Пример реализации обработки запроса пользователя
    и строки запроса'''
    return HttpResponse('<h1> О нас</h1>')

def contact(request):
    ''' Второй пример использования запроса пользлавтеля'''
    return HttpResponseRedirect("/firstapp/about/")

def detail(request):
    return HttpResponsePermanentRedirect('/firstapp/')

def products(request, productid):
    '''Функция для изучения получения данных из запроса url адреса
    http://127.0.0.1:8000/firstapp/produsts/2/'''
    return HttpResponse("<h1>Продукт № {0}".format(productid))

def users(request, id, name):
    '''Функйия получения данныйх из URL запроса
    http://127.0.0.1:8000/firstapp/users/2/Maria/'''
    return HttpResponse("<h1>Привет {0} ваш id:{1}</h1>".format(name, id))

def blanks(request, blankid, name, phone):
    '''Моя функция для того чтобы пронять правильно ли получил как вытащить переменные из URL запроса
    http://127.0.0.1:8000/firstapp/blanks/1/Maria/89089462235/'''
    page ="<h1>Номер бланка {0}, заполнен на {1}, телефон {2} </h1>".format(blankid, name, phone)
    return HttpResponse(page)

def mod_products(request, productid = 2):
    '''Функция для изучения получения данных из запроса url адреса
    если не запрлнино поле запроса можно поставить значение по умолчанию
    http://127.0.0.1:8000/firstapp/produsts/'''
    return HttpResponse("<h1>Продукт № {0}".format(productid))

def posts(request, id = 1):
    '''Попытка достать данные из URL через функцию path(),'''
    if id == 1:
        return HttpResponse('<h1>Posts list</h1>')
    else:
        return HttpResponse("<h1> Post №{0}.".format(id))

def posts_edit(request, id):
    '''Пост едит с адишником'''
    if id == 1:
        return HttpResponse('<h1>Posts list</h1>')
    else:
        return HttpResponse("<h1>Edit posts № {0}</h1>".format(id))

def posts_name(request, id =1, name = 'Gleb'):
    if id == 1:
        return HttpResponse('<h1>Posts list</h1>')
    else:
        if request.GET.get('pk','1') != '':
            return HttpResponse('<h1> Edit posts № {0}: author: {1}, Request get = {2} , категория = {3}'.format(id, name, request.GET.get('pk', '1'), request.GET.get('kategori', 'default')))
        return HttpResponse("<h1>Edit posts № {0}: author: {1}</h1>".format(id, name))