import os
from array import array
from os.path import normpath

from django.conf.urls import url
from django.contrib.sessions.backends import file
from django.shortcuts import render, redirect, get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from django.views.generic import CreateView

from .forms import UserForm, HelperTextContactForm, CharFieldForm, SlugFieldForm, UrlFieldForm, UuiFieldForm, \
    ComboFieldForm, FilePathFieldForm, FileFieldForm, DateFieldForm, TimeFieldForm, DateTimeFieldForm, WidgetForm, \
    ThinTinctureForm, UserBookForm, CreatePerson, ChangeDataPersonModel, UpdateColumnForm, UpdatePerson, DeletePerson, \
    ElectricForm, ForestForm, TreeForm, TreeFormM, BugForm, AddBushInBug, BugBushClear, BushForm, BushFormForEdit, \
    SearchForm

# Create your views here.
from .models import Person, Electric, Forest, Tree, Bug, Bush
from django.db.models import F
from .utils import update_post, update_post_f, update_post_update_or_create, update_persons
from django.urls import reverse


# todo посмотреть подробнее про формы https://djangodoc.ru/3.2/topics/class-based-views/generic-editing/
# todo посмотреть миксины https://djangodoc.ru/3.2/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.initial
class TreeView(CreateView):
    model = Tree
    fields = ['name', 'height']


def index(request):
    css_class_btn = 'class=\"btn btn-info\"'
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
    content += '<a href="/firstapp/m304" class="btn btn-info">Error 304</a><br>'
    content += '<a href="/firstapp/m400" class="btn btn-info">Error 400</a><br>'
    content += '<a href="/firstapp/m403" class="btn btn-info">Error forbidden</a><br>'
    content += '<a href="/firstapp/m404" class="btn btn-info">Error 404 file not found</a><br>'
    content += '<a href="/firstapp/index_app3" class="btn btn-info">Связь шаблонов base.html и index_app3.html</a><br>'
    content += '<a href="/firstapp/about_template/" class="btn btn-info">Связь шаблонов base.html и about_template.html</a><br>'
    content += '<a href="/firstapp/if_template/" class="btn btn-info">Функция if в шаблоне</a><br>'
    content += '<a href="/firstapp/for_template/" class="btn btn-info">Функция for в шаблоне</a><br>'
    content += '<hr>'
    content += '<a href="/firstapp/form_template/" class="btn btn-info">Формы</a><br>'
    content += '<a href="/firstapp/form_helper_text/" class="btn btn-info">Форма Helper text</a><br>'
    content += '<a href="/firstapp/form_char_field/" class="btn btn-info">Форма Char Field</a><br>'
    content += '<a href="/firstapp/slug_field_form/" class="btn btn-info">Форма Slug field</a><br>'
    content += '<a href="/firstapp/url_field_form/" class="btn btn-info">Форма Url field</a><br>'
    content += '<a href="/firstapp/uuid_field_form/" class="btn btn-info">Форма Uuid field</a><br>'
    content += '<a href="/firstapp/combo_field_form/" class="btn btn-info">Форма Combo field</a><br>'
    content += '<a href="/firstapp/file_path_field_form/" class="btn btn-info">Форма File path field</a><br>'
    content += '<a href="/firstapp/date_field_form/" class="btn btn-info">Форма Date field</a><br>'
    content += '<a href="/firstapp/time_field_form/" class="btn btn-info">Форма Time field</a><br>'
    content += '<a href="/firstapp/date_time_field_form/" class="btn btn-info">Форма Date time field</a><br>'
    content += '<a href="/firstapp/widget_form/" class="btn btn-info">Форма изменеия Widget</a><br>'
    content += '<a href="/firstapp/thin_tincture_form/" class="btn btn-info">Форма тонкая настройка формы</a><br>'
    content += '<a href="/firstapp/user_book_form/" class="btn btn-info">Тонкая настройка из кникги формы</a><br>'
    content += '<a href="/firstapp/css_class_form/" class="btn btn-info">Форма из книги с настройкой css из класса ' \
               'формы</a><br> '
    content += '<a href="/firstapp/attrs_css_form/" class="btn btn-info">Вытащить css из attrs</a><br> '
    content += '<hr>'
    content += '<a href="/firstapp/create_person/" class="btn btn-info">Заполнение таблицы модели при помощи формы</a><br> '
    content += '<a href="/firstapp/method_get_person/15/" class="btn btn-info">Функция get модели</a><br> '
    content += '<a href="/firstapp/method_get_or_create_person/" class="btn btn-info">Функции get_or_created модели</a><br> '
    content += '<a href="/firstapp/method_filter_person/" class="btn btn-info">Функции filter модели</a><br> '
    content += '<a href="/firstapp/method_exclude_model/" class="btn btn-info">Функции exclude модели</a><br> '
    content += '<a href="/firstapp/method_in_bulk_model/" class="btn btn-info">Функции in_bulk модели</a><br> '
    content += '<a href="/firstapp/change_date_in_bd/" class="btn btn-info">Функции save модели</a><br> '
    content += "<a href=\"{0}\" class=\"btn btn-info\">Функции save, save(update_fields=\'name\') модели</a><br>".format(
        'update_bd_person')
    content += "<a href=\"{0}\" class=\"btn btn-info\">Функции F обновлние всего столбика модели</a><br>".format(
        'metod_f')
    content += "<a href=\"{0}\" class=\"btn btn-info\">Обновление несеолько столбикоа методом filter</a><br>".format(
        'metod_filter_update')
    content += "<a href=\"{0}\" class=\"btn btn-info\">Обновление нескольких полей методом filter().update() + F()</a><br>".format(
        'method_filter_update_and_f')
    content += "<a href=\"{0}\" class=\"btn btn-info\">Обновление нескольких полей методом method_update_or_create</a><br>".format(
        'method_update_or_create')
    content += "<a href=\"person/8/delete/\" class=\"btn btn-info\">Удаляет данные по get запросу</a><br>"
    content += "<a href=\"person/8/delete/\" class=\"btn btn-info\">Удаляет данные по get запросу</a><br>"
    content += "<a href=\"{0}\" class=\"btn btn-info\">Все персоны</a><br>".format('index_persons')
    content += "<a href=\"{0}\" class=\"btn btn-info\">Все персоны, из учебника</a><br>".format('index_crude')
    content += "<a href=\"{0}\" {1}>Все элекстрики</a><br>".format('electric_index', css_class_btn)
    content += "<hr>"
    content += "<a href=\"{0}\" {1}>Один ко многим Лес деревья</a><br>".format('index_forest', css_class_btn)
    content += "<a href=\"{0}\" {1}>Многие ко многим Жуки кусты создание</a><br>".format('index_bug/1/bush/2/create', css_class_btn)
    content += "<a href=\"{0}\" {1}>Многие ко многим Жуки</a><br>".format('index_bug/', css_class_btn)
    content += "<a href=\"{0}\" {1}>Многие ко многим Кусты</a><br>".format('bush_index/', css_class_btn)

    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    return render(request, 'firstapp/home.html', {'content': content, 'file': path_file})


def def_template_render(request):
    return TemplateResponse(request, 'firstapp/templsteRespond.html')


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
    page = "<h1>Номер бланка {0}, заполнен на {1}, телефон {2} </h1>".format(blankid, name, phone)
    return HttpResponse(page)


def mod_products(request, productid=2):
    '''Функция для изучения получения данных из запроса url адреса
    если не запрлнино поле запроса можно поставить значение по умолчанию
    http://127.0.0.1:8000/firstapp/produsts/'''
    return HttpResponse("<h1>Продукт № {0}".format(productid))


def posts(request, id=1):
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


def posts_name(request, id=1, name='Gleb'):
    if id == 1:
        return HttpResponse('<h1>Posts list</h1>')
    else:
        if request.GET.get('pk', '1') != '':
            return HttpResponse(
                '<h1> Edit posts № {0}: author: {1}, Request get = {2} , категория = {3}'.format(
                    id, name, request.GET.get('pk', '1'), request.GET.get('kategori', 'default')))
        return HttpResponse("<h1>Edit posts № {0}: author: {1}</h1>".format(id, name))


def m304(request):
    return HttpResponseNotModified()


def m400(request):
    '''Ошибка 400'''
    return HttpResponseBadRequest("<h1> Bad request </h1> ")


def m403(request):
    '''Ошибка 403'''
    return HttpResponseForbidden('<h1>Forbidden</h1>')


def m404(request):
    '''Ошибка 404 file not found'''
    return HttpResponseNotFound('<h1> File not found </h1>')


def index_app1(request):
    '''Передача данных в шаблон пункт 5.3'''
    data = {"header": "Пердача данных в шаблон",
            "message": "Загружен шаблон fitstapp/templates/firstapp/index_app1.html"
            }
    return render(request, 'firstapp/index_app1.html', context=data)


def index_app2(request):
    '''Передача сложных данных'''
    header = "Персональные данные"
    langs = ["Английский", "Немецкий", "Испанский"]
    user = {"name": "Максим", "age": 18}
    adr = ("Виноградная", 25, 25)
    data = {"header": header, "langs": langs, "user": user, "address": adr}
    return render(request, 'firstapp/index_app2.html', context=data)


def index_app3(request):
    '''Пример связки базового шаблона и индекса'''
    return render(request, 'firstapp/index_app3.html')


def about_template(request):
    '''Связь шаблонов base.html и about_template.html'''
    return render(request, 'firstapp/about_template.html')


def if_template(request):
    '''Шаблон с функцией if внутри'''
    data = {"age": 18}
    return render(request, 'firstapp/if_template.html', context=data)


def for_template(request):
    '''Обработка for в шаблоне'''
    array_template = ['Шнурок', "сосиска", "Ноутбуки", "Принтеры"]
    # array_template = [] #проверка функции {% empty %}
    data = {"array": array_template}
    return render(request, 'firstapp/for_template.html', context=data)


def form_template(request):
    """Шаблон для изучения форм в django"""
    if request.method == 'POST':
        name = request.POST.get('name')  # Получить данные из формы поля name
        age = request.POST.get('age')  # Получить данные из формы поля age
        output = "<h2>Имя: {0}, возраст {1} </h2>".format(name, age)
        return HttpResponse(output)
    else:
        # Если форма не пришла еще то отправляем шаблон с формой
        user_form = UserForm(label_suffix='?')  # Создаем обьект формы
        return render(request, 'firstapp/form_template.html', {"user_form": user_form})


def form_helper_text(request):
    """Обработчик для HelpTextContactForm"""
    if request.method == 'POST':  # Если форма была отправлена
        subject = request.POST.get('subject')  # Извлекаем данные из request запроса
        message = request.POST.get('message')  #
        sender = request.POST.get('sender')  #
        cc_my_self = request.POST.get('cc_my_self')  #
        return HttpResponse("<p>Тема: {0}</p>"  # Делаем с данными что хотим
                            "<p>Сообшение: {1}</p>"  # перенаправляема в шаблон для ответа пользователю
                            "<p>Емайл: {2} </p>"
                            "<p>Галочка: {3} </p>".format(subject, message, sender, cc_my_self))
    else:
        helper_form = HelperTextContactForm(auto_id=False)
        return render(request, 'firstapp/form_helper_text.html', {'helper_form': helper_form})


def form_char_field(request):
    """ CharField изучение поля"""
    if request.method == 'POST':
        form_char = CharFieldForm(request.POST)
        if form_char.is_valid():
            name = form_char.cleaned_data['name']
            error = form_char.errors
            return HttpResponse('<h1>Имя: {0} </h1>'.format(name))
        else:
            return HttpResponse('<h1>Ошибка введено неверное имя</h1>')
    else:
        form_char = CharFieldForm(field_order=["message", "name", "email", "ip_address", "reg_text"])
        return render(request, 'firstapp/form_char_field.html', {"form_char": form_char})


def slug_field_form(request):
    """SlugField"""
    if request.method == 'POST':
        slug_form = SlugFieldForm(request.POST)
        if slug_form.is_valid():
            slug = slug_form.cleaned_data
            return HttpResponse('Valid is sacsessful <br> Slug: {0}'.format(slug))
        else:
            slug_errors = slug_form.errors
            return HttpResponse("We find error: <br> {0}".format(slug_errors))
    else:
        slug_form = SlugFieldForm()
        return render(request, template_name="firstapp/slug_field_form.html", context={"slug_form": slug_form})


def url_field_form(request):
    """Url field from book"""
    url_form = UrlFieldForm()
    return render(request, template_name='firstapp/url_field_form.html', context={"form": url_form})


def uuid_field_form(request):
    """"Comment uuid form"""
    if request.method == 'POST':
        uuid = request.POST.get("uui")
        return HttpResponse('<h1> UUID: {0} '.format(uuid))
    else:
        uuid_form = UuiFieldForm()
        return render(request, 'firstapp/uui_field_form.html', context={"form": uuid_form})


def combo_field_form(request):
    """Combo field"""
    combo_form = ComboFieldForm()
    return render(request, 'firstapp/combo_field_form.html', context={"form": combo_form})


def file_path_field_form(request):
    """File path field"""
    title = 'File path field'
    # Проверка пришла ли форма
    if request.method == 'POST':
        file_path = request.POST.get('file_path')
        return HttpResponse("<h3>Путь: {0}</h3>".format(file_path))
    else:
        file_path_form = FilePathFieldForm()
        return render(request, 'firstapp/universal_form_template.html',
                      context={"title": title, "header": title, "form": file_path_form})


def handle_uploaded_file(file):
    pass
    destination = open('F:\\', 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()


def file_field_form(request):
    """File field form"""
    # TODO Разобраться с загрузокой файлов есть какойто SimpleUpload
    title = "File field"
    # Проверка была ли отправлена на сервер форма
    if request.method == 'POST':
        file_form = FileFieldForm(request.POST, request.FILES)
        if file_form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('Успешно загружен')
        else:
            # form = FileFieldForm()
            errors = file_form.errors
            return HttpResponse('Неудалось загрузить файл {0} <br> {1}'.format(request.FILES, request.POST))
    else:
        form = FileFieldForm()
        return render(request, 'firstapp/universal_form_template.html',
                      context={"title": title, "header": title, "form": form})


def date_field_form(request):
    """Date field"""
    title = 'Data field'
    if request.method == 'POST':
        date = request.POST.get('date')
        return HttpResponse("Date: {0}".format(date))
    else:
        form = DateFieldForm()
        return render(request, 'firstapp/universal_form_template.html',
                      context={"title": title, "header": title, "form": form})


def time_field_form(request):
    """Time field"""
    title = 'Time form'
    form = TimeFieldForm(auto_id=False)
    return render(request, 'firstapp/universal_form_template.html',
                  context={"title": title, "header": title, "form": form})


def date_time_field_form(request):
    """Date time field"""
    title = 'Date time field'

    # проверка отправленна ли форма
    if request.method == 'POST':
        form = DateTimeFieldForm(request.POST)
        if form.is_valid():
            date_time = form.cleaned_data['date_time']
            return HttpResponse('Date: {0}'.format(date_time))
        else:
            errors = form.errors
            return HttpResponse('not valid form {0}'.format(errors))
    else:
        form = DateTimeFieldForm()
        return render(request, 'firstapp/universal_form_template.html',
                      context={"title": title, "header": title, "form": form})


def widget_form(request):
    """Запрос формы в которой изменим виджет"""
    title = 'Запрос формы в которой изменим виджет'
    if request.method == 'POST':
        widget_form = WidgetForm(request.POST)
        if widget_form.is_valid():
            name = widget_form.cleaned_data['name']
            age = widget_form.cleaned_data['age']
            comment = widget_form.cleaned_data['comment']
            return HttpResponse("Name: {0}<br> Age: {1}<br> Comment: {2}".format(name, age, comment))
        else:
            return HttpResponse(widget_form.errors)
    else:
        form = WidgetForm(field_order=["age", "comment", "name"])
        return render(request, 'firstapp/universal_form_template.html',
                      context={"title": title, "header": title, "form": form})


def thin_tincture_form(request):
    """Тонкая настройка формы"""
    title = 'Тонкая настройка формы'
    err_age = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        form = ThinTinctureForm(request.POST)
        err_age = form.errors
        return HttpResponse(
            "name: {0}<br> age: {1}<br> comment: {2}<br> error_messages {3}".format(name, age, comment, err_age))
    else:
        form = ThinTinctureForm()
        return render(request, 'firstapp/thin_tincture_template.html',
                      context={"title": title, "header": title, "form": form})


def user_book_form(request):
    title = 'Тонкая настройка формы из книги'
    user_form = UserBookForm()
    if request.method == 'POST':
        user_form = UserBookForm(request.POST)
        if user_form.is_valid():
            name = user_form.cleaned_data['name']
            return HttpResponse("Вы ввели имя: {0}".format(name))
        else:
            return HttpResponse("Ошибка <br> {0}".format(user_form.errors))
    else:
        return render(request, 'firstapp/user_book_form.html', context={"title": title, "form": user_form})


def css_class_form(request):
    title = 'Тонкая настройка формы из книги'
    user_form = UserBookForm()
    if request.method == 'POST':
        user_form = UserBookForm(request.POST)
        if user_form.is_valid():
            name = user_form.cleaned_data['name']
            return HttpResponse("Вы ввели имя: {0}".format(name))
        else:
            return render(request, 'firstapp/css_class_form.html', context={"title": title, "form": user_form})
    else:
        return render(request, 'firstapp/css_class_form.html', context={"title": title, "form": user_form})


def attrs_css_form(request):
    """Тонкая настройка формы"""
    title = 'Тонкая настройка формы'
    err_age = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        form = ThinTinctureForm(request.POST)
        err_age = form.errors
        return HttpResponse(
            "name: {0}<br> age: {1}<br> comment: {2}<br> error_messages {3}".format(name, age, comment, err_age))
    else:
        form = ThinTinctureForm()
        return render(request, 'firstapp/attrs_css_form.html',
                      context={"title": title, "header": title, "form": form})


def create_person(request):
    """Начало модели Личность"""
    title = 'Начало модели Личность'
    create_person_form = CreatePerson()
    if request.method == 'POST':
        create_person_form = CreatePerson(request.POST)
        if create_person_form.is_valid():
            is_create_person = create_person_form.cleaned_data['is_create']
            if is_create_person == True:
                for years in range(30):
                    person = Person(name="igor", age=years)
                    person.save()

                persons = Person.objects.all()
                return render(request, 'firstapp/create_person.html',
                              context={"title": title, "person": create_person_form, "persons": persons})
        else:
            return render(request, 'firstapp/create_person.html',
                          context={"title": title, "person": create_person_form})
    else:
        return render(request, 'firstapp/create_person.html', context={"title": title, "person": create_person_form})


def method_get_person(request, id):
    """Метод модели get"""
    id = int(id)
    try:
        first_person = Person.objects.get(id=id)
        second_person = Person.objects.get(name='igor')
    except Person.DoesNotExist:  # Вызывает исключения когда не нащел Id в таблице
        return HttpResponse('not this id')
    except Person.MultipleObjectsReturned as me:  # Вызывает когда собподений больше одного
        second_person = {"name": me}
    return render(request, 'firstapp/method_person.html',
                  context={"title": 'Методы модели', "first_person": first_person, "second_person": second_person})


def method_get_or_create_person(request):
    """Метод get_or_create обязательно должны быть заполнены все обязательные поля можели !!! иначе исключение вызовет"""
    iror, created = Person.objects.get_or_create(id=800, name='Igor',
                                                 age=12)  # created = True если объект будет создан заново
    return render(request, 'firstapp/method_get_or_create_model.html',
                  context={"title": 'Метод get_or_create', "igor": iror, "created": created})


def method_filter_person(request):
    """Метод filter извлекает из базы все что подошло под фильтер"""
    persons = Person.objects.filter(age=12)  # Находим все строки которые соответствуют фильтру
    return render(request, 'firstapp/method_filter_model.html', context={"title": 'Метод filter', "persons": persons})


def method_exclude_model(request):
    """Метод exclude- уберает из выборки данные соответствеющие условию"""
    persons = Person.objects.exclude(age=12)
    iteration = 0
    type_exclude = str(type(persons))
    return render(request, 'firstapp/methon_exclude_model.html',
                  context={"title": 'Метод excude- уберает из выборки данные соответствеющие условию',
                           "persons": persons, "i": iteration, "type_exclude": type_exclude})


def method_in_bulk_model(request):
    """Метод in_bulk - похоже тоже самое что и фильт только возвращает результат в виде словаря"""
    # TODO Не понял до конца как работает in_bulk
    persons = Person.objects.in_bulk()
    type_exclude = str(type(persons))
    persons_bulk = {}
    for ids in persons:
        persons_bulk['id'] = persons[ids].id
        print(persons[ids])
    return render(request, 'firstapp/methon_in_bulk_model.html',
                  context={
                      "title": 'Метод in_bulk - похоже тоже самое что и фильт только возвращает результат в виде словаря',
                      "persons": persons_bulk, "type_exclude": type_exclude})


def change_date_in_bd(request):
    """ Меняем данные модели Person из формы """
    title = ' Меняем данные модели Person из формы '
    messages = ''
    form = ChangeDataPersonModel()
    if request.method == 'POST':
        form = ChangeDataPersonModel(request.POST)
        if form.is_valid():
            messages = 'Форма успешно получена'
            # извлекаем данные из формы
            id_person = form.cleaned_data['id_person']
            name = form.cleaned_data['name']
            age = int(form.cleaned_data['age'])
            only_name = form.cleaned_data['only_name']
            # пробуем получить обьект из базы данных
            try:
                person = Person.objects.get(id=id_person)
            except Person.DoesNotExist:
                messages = 'Данной записи в базе нет'
            except:
                messages = 'Что-то пошло не так'
            # пепеправляем данные в полученый объект базы данных
            person.name = name
            person.age = age
            if only_name == True:  # Если стоит галочка записывает только name
                Person.objects.filter(id=id_person).update(name=name)
                print("work")
            else:
                person.save()  # Сохраняем в БД
                print("not work")
            messages += ' и сохранен в базе данных.'
            return render(request, 'firstapp/change_date_in_bd.html',
                          context={"title": title, "header": title, "form": form, "messages": messages,
                                   "person": person})

        else:
            return render(request, 'firstapp/change_date_in_bd.html',
                          context={"title": title, "header": title, "form": form, "messages": messages})
    else:
        return render(request, 'firstapp/change_date_in_bd.html',
                      context={"title": title, "header": title, "form": form, "messages": messages})


def update_bd_person(request):
    """update - должен сохранять вроде только часть талбицы но чегото сохраняет все поля"""
    title = ' Меняем данные модели Person из формы методом person.save(fields_update=\'name\''
    messages = ''
    form = ChangeDataPersonModel()
    if request.method == 'POST':
        form = ChangeDataPersonModel(request.POST)
        if form.is_valid():
            messages = 'Форма успешно получена'
            # извлекаем данные из формы
            id_person = form.cleaned_data['id_person']
            name = form.cleaned_data['name']
            age = int(form.cleaned_data['age'])
            only_name = form.cleaned_data['only_name']
            # пробуем получить обьект из базы данных
            try:
                person = Person.objects.get(id=5)
            except Person.DoesNotExist:
                messages = 'Данной записи в базе нет'
            except:
                messages = 'Что-то пошло не так'
            # пепеправляем данные в полученый объект базы данных
            person.name = name
            person.save(update_fields=['name'])  # Сохраняем в БД
            messages += ' и сохранен в базе данных.'
            return render(request, 'firstapp/change_date_in_bd.html',
                          context={"title": title, "header": title, "form": form, "messages": messages,
                                   "person": person})

        else:
            return render(request, 'firstapp/change_date_in_bd.html',
                          context={"title": title, "header": title, "form": form, "messages": messages})
    else:
        return render(request, 'firstapp/change_date_in_bd.html',
                      context={"title": title, "header": title, "form": form, "messages": messages})


def metod_f(request):
    """Меняет весь столбец"""
    title = 'Меняет весь столбец'
    messages = ''
    persons = Person.objects.all()
    form = UpdateColumnForm()
    if request.method == 'POST':
        form = UpdateColumnForm(request.POST)
        if form.is_valid():
            delta_age = int(form.cleaned_data['delta_age'])
            persons.update(age=F('age') + 1)
            return render(request, 'firstapp/metod_f.html',
                          context={"title": title, "header": title, "form": form, "messages": messages,
                                   "persons": persons})
        else:
            return render(request, 'firstapp/metod_f.html',
                          context={"title": title, "header": title, "form": form, "messages": messages,
                                   "persons": persons})
    else:
        return render(request, 'firstapp/metod_f.html',
                      context={"title": title, "header": title, "form": form, "messages": messages, "persons": persons})


def method_filter_update(request):
    """Обновление нескольких полей методом filter().update()"""
    title = 'Обновление нескольких полей методом filter().update()'
    messages = ''
    persons = Person.objects.all()
    form = UpdatePerson()
    return update_post(request, persons, form, 'firstapp/metod_filter_update.html', title, messages)


def method_filter_update_and_f(request):
    """Обновление нескольких полей методом filter().update() + F()"""
    title = 'Обновление нескольких полей методом filter().update()'
    messages = ''
    persons = Person.objects.all()
    form = UpdatePerson()
    return update_post_f(request, persons, form, 'firstapp/metod_filter_update.html', title, messages)


def method_update_or_create(request):
    """Обновление полей методом update_or_create"""
    title = 'Обновление нескольких полей методом filter().update()'
    messages = ''
    persons = Person.objects.all()
    form = UpdatePerson()
    return update_post_update_or_create(request, persons, form, 'firstapp/metod_filter_update.html', title, messages)


def method_delete_person(request, id_person):
    """ Удаляет данные по get запросу"""
    title = 'Меняет весь столбец'
    messages = ''
    persons = Person.objects.all()
    form = UpdatePerson()
    delete_form = DeletePerson()
    messages = "{}".format(str(id_person))
    context = {"title": title, "header": title, "form": form, "messages": messages, "persons": persons,
               "delete_form": delete_form}
    if request.method == 'POST':  # Проверели форму что нам ее отправили методом пост
        delete_form = DeletePerson(request.POST)  # Передали запрос в форму
        if delete_form.is_valid():  # Проверили вылидна ли форма
            id_person = delete_form.cleaned_data['id_person']  # Извлекли данные из формы
            try:  # Попытка удаления обьекта
                person = Person.objects.get(id=id_person)  # Найти и извлеч объект из базы данных
                person.delete()  # Если нашли удалить
                context['messages'] = "Запись id:{0} удалена".format(
                    id_person)  # Сообщить об успешном удалении пользователю
                context['persons'] = Person.objects.all()
                return render(request, 'firstapp/metod_f.html', context=context)
            except Person.DoesNotExist:
                context['messages'] = 'Данной записи не существует'
                return render(request, 'firstapp/metod_f.html', context=context)
            except Person.MultipleObjectsReturned as e:
                context['messages'] = "{}".format(e)
                return render(request, 'firstapp/metod_f.html', context=context)
        else:
            context['messages'] = delete_form.errors
            return render(request, 'firstapp/metod_f.html', context=context)
    else:
        return render(request, 'firstapp/metod_f.html', context=context)


def index_persons(request):
    """Таблица всех Persons"""
    title = 'Обновление нескольких полей методом filter().update()'
    messages = ''
    template = 'firstapp/index_persons.html'
    persons = Person.objects.all()
    form = UpdatePerson()
    delete_form = DeletePerson()
    context = {"title": title, "header": title, "form": form, "messages": messages,
               "persons": persons, "delete_form": delete_form}
    """Функция для обновления данных в модели"""
    if request.method == 'POST':
        form = UpdatePerson(request.POST)
        if form.is_valid():
            id_person = int(form.cleaned_data['id_person'])
            name = str(form.cleaned_data['name'])
            age = int(form.cleaned_data['age'])
            bio = str(form.cleaned_data['bio'])
            data_for_defaults_person = {"name": name, "age": age, "bio": bio}
            person, created = Person.objects.update_or_create(id=id_person, defaults=data_for_defaults_person)
            if created == True:
                context['messages'] = 'Записи нет в базе данных, персона была добаленеа'
            return render(request, template, context=context)
        else:
            return render(request, template, context=context)
    else:
        return render(request, template, context=context)


def index_crude(request):
    """Индексный файл из учебника, получение всех данных из модели"""
    title = ''
    messages = ''
    persons = Person.objects.all()
    return render(request, 'firstapp/index_crude.html', context={"persons": persons})


def create(request):
    """Созданик персоны, по пост запросу из формы"""
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect('index_crude')


def edit(request, id_person):
    """Изменение данных в ДБ"""
    title = ''
    try:
        person = Person.objects.get(id=id_person)
        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return HttpResponseRedirect("/firstapp/index_crude")
        else:
            return render(request, 'firstapp/edit.html', context={"person": person, "title": title})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Клиент не найден</p>')


def delete(request, id):
    """Удаление базы из данных"""
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/firstapp/index_crude")
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h1>Данная записть не найдена</h1>')


def electric_index(request):
    """Создать индексный файл и вывести всех электриков"""
    title = ''
    context = {}
    try:  # Попытка передать данные из другой функции
        context['messages'] = request.session['messages']
        request.session.pop('messages')
    except KeyError:
        pass
    form = ElectricForm()
    context['form'] = form
    electrics = Electric.objects.all()
    context['electrics'] = electrics
    return render(request, 'firstapp/electric_index.html', context=context)


def electric_new(request):
    """Create new electrical"""
    if request.method == 'POST':
        form = ElectricForm(request.POST)
        electric = Electric()
        if form.is_valid():
            electric.name = form.cleaned_data['name']
            electric.dict = form.cleaned_data['dict']
            electric.email = form.cleaned_data['email']
            electric.bio = form.cleaned_data['bio']
            electric.active = form.cleaned_data['active']
            electric.save()
            return redirect('electric_index')
        else:
            return HttpResponse('Не удалось пройти валидацию формы')
    else:
        return HttpResponseRedirect(reverse('electric_index'))


def electric_edit(request, pk):
    """Редактирование профиля электрика"""
    title = 'Редактирование профиля электрика'
    context = {}
    context['messages'] = ''
    context['title'] = title
    form = ElectricForm()
    context['form'] = form
    try:  # Пробуем найти в базе данных профиль электрика
        electric = Electric.objects.get(pk=pk)
        form = ElectricForm(instance=electric)
        context['form'] = form
        if request.method == 'POST':
            form = ElectricForm(request.POST)
            if form.is_valid():  # Провека формы
                electric.name = form.cleaned_data['name']
                electric.bio = form.cleaned_data['bio']
                electric.active = form.cleaned_data['active']
                electric.dict = form.cleaned_data['dict']
                electric.save()  # Сохранение профиля в базе данных
                context['form'] = ElectricForm(instance=electric)
                context['messages'] = str(electric.id)
                request.session['messages'] = context['messages']
                return redirect(reverse('electric_index'), context=context)  # Рендерим форму с изменениями
            else:
                context['messages'] = form.errors
                return render(request, 'firstapp/electric_edit.html', context=context)
        else:  # метод get
            return render(request, 'firstapp/electric_edit.html', context=context)
    except Electric.DoesNotExist:
        return HttpResponse('Данного профиля электрика не существует')
    return redirect('electric_index')


def electric_delete(request, pk):
    """Функция удаления профиля электрика из БД"""
    try:
        electric = Electric.objects.get(pk=pk)
        electric.delete()
        request.session['messages'] = "Профиль id: {0} успешно удален".format(pk)
        return redirect(reverse('electric_index'))
    except Electric.DoesNotExist:
        return HttpResponse('Данный профиль не найден')


def index_forest(request):
    """Индекс форест"""
    forests = Forest.objects.all()
    form = ForestForm()
    context = {}
    form_tree = TreeForm()
    context['form_tree'] = form_tree
    try:
        context['messages'] = request.session['messages']
        request.session.pop('messages')
    except KeyError:
        pass
    context['title'] = 'Модель один ко многим'
    context['forests'] = forests
    context['form'] = form
    return render(request, 'firstapp/index_forest.html', context=context)


def create_forest(request):
    """Create forest"""
    form = ForestForm()
    if request.method == 'POST':
        forest = Forest()
        form = ForestForm(request.POST)
        if form.is_valid():
            forest.name = form.cleaned_data['name']
            forest.save()
            request.session['messages'] = 'Лес успешно сохранен'
            return redirect(edit_forest, forest.id)
        else:
            request.session['messages'] = form.errors
            return render(request, 'firstapp/index_forest.html')
    else:
        return redirect(index_forest)


def edit_forest(request, id_forest):
    """Редактирование леса"""
    context = {}
    context['title'] = 'Редактирование леса'
    form = ForestForm()
    context['form'] = form
    form_tree = TreeForm()
    context['form_tree'] = form_tree

    # устанавливаем у формы создания нового дерева id нужного леса
    forest = get_object_or_404(Forest, pk=id_forest)
    tree = Tree(forest=forest)
    form_tree_m = TreeFormM(instance=tree)
    context['form_tree_m'] = form_tree_m
    try:
        context['messages'] = request.session['messages']
        request.session.pop('messages')
    except KeyError:
        pass
    try:
        forest = Forest.objects.get(pk=id_forest)  # .objects.get(pk=pk)
        context['forest'] = forest
        trees = forest.tree_set.all()
        context['trees'] = trees
        form = ForestForm(instance=forest)
        context['form'] = form
        if request.method == 'POST':
            form = ForestForm(request.POST)
            if form.is_valid():  # Проверка формы на ошибки
                forest.name = form.cleaned_data['name']
                forest.save()
                context['form'] = ForestForm(instance=forest)
                context['messages'] = "Лес id:{0} успешно изменен".format(id_forest)
                return render(request, 'firstapp/edit_forest.html', context=context)
            else:  # форма с ошибками
                context['messages'] = form.errors
                return render(request, 'firstapp/edit_forest.html', context=context)
        else:  # get запрос
            return render(request, 'firstapp/edit_forest.html', context=context)

    except Forest.DoesNotExist:
        request.session['messages'] = "Леса с id: {0} не найдено в базе данных".format(index_forest)
        return redirect(index_forest)


def delete_forest(request, id_forest):
    """Удаление леса"""
    # тут должна быть проверка на зпрос пост и на права пользователя
    try:
        forest = Forest.objects.get(pk=id_forest)
        forest.delete()
        request.session['messages'] = "Лес с id: {0} по имени: {1} удален.".format(forest.id, forest.name)
        return redirect(index_forest)
    except Forest.DoesNotExist:
        request.session['messages'] = "Данный лес не существует"
        return redirect(index_forest)


def create_tree(request, id_forest):
    """Добавление нового дерева в лес"""
    forest = get_object_or_404(Forest, pk=id_forest)
    if request.method == 'POST':
        # Излекаем данные из формы
        name = request.POST.get('name')
        height = request.POST.get('height')

        # Проверяем заполнена ли форма
        if (height != '') and (name != ''):
            tree = Tree(name=name, height=height)
            forest.tree_set.add(tree, bulk=False)
            request.session['messages'] = "Дерево успешно добавлено в лес"
            return redirect(edit_forest, forest.id)
        else:  # Если нет отправляем обратно на индексный файл с сообщением
            request.session['messages'] = 'В форме не заполнен один или несколько элеметов'
            return redirect(index_forest)
    else:
        request.session['messages'] = 'Дерево не добавлено отправте данные через форму'
        return redirect(index_forest)


def edit_tree(request, id_forest, id_tree):
    """Редактирование """
    context = {}
    tree = get_object_or_404(Tree, pk=id_tree)
    context['tree'] = tree
    forest = get_object_or_404(Forest, pk=id_forest)
    context['forest'] = forest
    context['form'] = TreeForm()
    if request.method == 'POST':
        # Излекаем данные из формы
        name = request.POST.get('name')
        height = request.POST.get('height')

        # Проверяем заполнена ли форма
        if (height != '') and (name != ''):
            tree = Tree(pk=id_tree, name=name, height=height)
            forest.tree_set.add(tree, bulk=False)
            request.session['messages'] = "Дерево успешно изменено в лесу"
            context['tree'] = tree
            context['forest'] = forest
            return render(request, 'firstapp/edit_tree.html', context=context)
        else:  # Если нет отправляем обратно на индексный файл с сообщением
            request.session['messages'] = 'В форме не заполнен один или несколько элеметов'
            return render(request, 'firstapp/edit_tree.html', context=context)
    else:
        request.session['messages'] = 'Дерево не добавлено отправте данные через форму'
        return render(request, 'firstapp/edit_tree.html', context=context)


def delete_tree(request, id_forest, id_tree):
    """Удаляет дерево по get запросу"""
    context = {}
    forest = get_object_or_404(Forest, pk=id_forest)
    context['forest'] = forest
    tree = get_object_or_404(Tree, pk=id_tree)
    context['tree'] = tree
    tree.delete()
    request.session['messages'] = "Дерево с id: {0} и названием: {1} удалено.".format(forest.id, id_tree)
    return redirect(edit_forest, forest.id)


def create_bug(request):
    """Создание жука """
    context = {}
    if request.method == 'POST':
        bug = Bug()
        form = BugForm(request.POST)
        if form.is_valid():
            bug.name = form.cleaned_data['name']
            bug.population = form.cleaned_data['population']
            bug.save()
            request.session['messages'] = 'Жук сохранен {0}'.format(bug.name)
            return redirect(index_bug)
    else:
        request.session['messages'] = 'Отправте форму POST запросом'
        return redirect(index_bug)


def index_bug(request):
    """Индексный файл жуков"""
    context = {}
    bugs = Bug.objects.all()
    context['bugs'] = bugs
    form = BugForm()
    context['form'] = form
    form_add_bush = AddBushInBug()
    context['form_add_bush'] = form_add_bush
    try:
        context['messages'] = request.session['messages']
        request.session.pop('messages')
    except KeyError:
        pass
    return render(request, 'firstapp/index_bugs.html', context=context)


def create_bug_and_bush(request, id_bug, id_bush):
    """Создать жуков и кусты"""
    context = {}
    bug = Bug.objects.create(name="Серебрянка {0}".format(id_bug), population=500)
    context['messages'] = bug.__str__() + '<br>'
    bug.bush_set.create(name="Малина {0}".format(id_bush))
    bush_malina = get_object_or_404(Bush, pk=2)
    context['messages'] += bush_malina.__str__() + '<br>'
    bugs = Bug.objects.all()
    context['messages'] += bugs.__str__() + '<br>'
    # добавить всех жуков на куст 1
    # for bug in bugs:
    #     bush_malina.bugs.add(bug)
    bugs_on_bush_malina = bush_malina.bugs.all()
    context['bush'] = bush_malina
    context['bugs'] = bugs_on_bush_malina
    # Удалить жуков с 17 по 22 id с куста
    # for id_bug in range(17, 23):
    #     bug = get_object_or_404(Bug, pk=id_bug)
    #     bush_malina.bugs.remove(bug)
    # Удаляем всех жуков с куста
    # bush_malina.bugs.clear()
    return render(request, 'firstapp/create_bug_in_bush.html', context=context)

def bug_edit(request, bug_id):
    """Edit bug по id"""
    context = {}
    bug = get_object_or_404(Bug, pk=bug_id)
    context['bug'] = bug
    form = BugForm(instance=bug)
    context['form'] = form
    context['form_clear'] = BugBushClear()
    try: # переносим сообщение из сессии в текущию функцию и видимость
        context['messages'] = request.session['messages']
        request.session.pop('messages')
    except KeyError:
        pass
    # Форма для добавления куста к жуку
    context['form_add_bush'] = AddBushInBug()
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            bug = form.save()
            bug = get_object_or_404(Bug, pk=bug_id)
            context['bug'] = bug
            context['form'] = form
            request.session['messages'] = 'Жук с id {0} изменен'.format(bug.id)
            return render(request, 'firstapp/edit_bug.html', context=context)
        else:
            request.session['messages'] = form.errors
            return render(request, 'firstapp/edit_bug.html', context=context)
    else:
        return render(request, 'firstapp/edit_bug.html', context=context)


def bug_add(request, id_bug):
    """Add bush к bug"""
    if request.method == 'POST':
        bug = get_object_or_404(Bug, pk=id_bug)
        form = AddBushInBug(request.POST)
        if form.is_valid():
            bush_id = form.cleaned_data['bush_id']
            bush = get_object_or_404(Bush, pk=bush_id)
            bug.bush_set.add(bush)
            request.session['messages'] = "Куст {0} добавлен к жуку {1}".format(bush.name, bug.name)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))


def bug_clear(request, bug_id):
    """Открепить куст от жука, не удаляя"""
    if request.method == 'POST':
        bug = get_object_or_404(Bug, pk=bug_id)
        form = AddBushInBug(request.POST)
        if form.is_valid():
            bush_id = form.cleaned_data['bush_id']
            bush = get_object_or_404(Bush,  pk=bush_id)
            bug.bush_set.remove(bush)
            request.session['messages'] = "Куст {0} откреплен от жука {1}".format(bush.name, bug.name)
            return redirect(index_bug)
        else:
            request.session['messages'] = form.errors
            return redirect(index_bug)
    else:
        request.session['messages'] = 'Отправте форму POST запросом'
        return redirect(index_bug)


def bug_edit_clear(request, bug_id, bush_id):
    """Открепляем жука от куста"""
    if request.method == 'POST':
        bug = get_object_or_404(Bug, pk=bug_id)
        bush = get_object_or_404(Bush, pk=bush_id)
        bug.bush_set.remove(bush)
        request.session['messages'] = "Куст {0} с id {1} откреплен от жука {2} c id {3}"\
            .format(bush.name, bush.id, bug.name, bug.id)

        return redirect(request.META.get('HTTP_REFERER'))
    request.session['messages'] = "Отправте запрос методом пост через форму"
    return redirect(request.META.get('HTTP_REFERER'))

def bug_clear_all(request, bug_id):
    """Очищает жука от кустов"""
    bug = get_object_or_404(Bug, pk=bug_id)
    bug.bush_set.clear()
    request.session['messages'] = "Жук {0} очищен от кустов".format(bug.name)
    return redirect(request.META.get('HTTP_REFERER'))


def bush_index(request):
    """Вывод всех кустов"""
    context = {}
    bushes = Bush.objects.all()
    context['bushes'] = bushes
    form = BushForm()
    context['form'] = form
    context['form_add_bush'] = AddBushInBug()
    context['form_clear'] = BugBushClear()
    try:
        context['messages'] = request.session['messages']
        request.session.pop('messages')
    except KeyError:
        pass
    return render(request, 'firstapp/index_bush.html', context=context)

def bush_create(request):
    """Создание формы"""
    if request.method == 'POST':
        bush = Bush()
        form = BushForm(request.POST, instance=bush)
        if form.is_valid():
            request.session['messages'] = form.cleaned_data['bug_id']
            form.save()
            return redirect(bush_index)
        else:
            request.session['messages'] = form.errors
            return redirect(bush_index)
    else:
        request.session['messages'] = 'Отправте запрос методом get'
        return redirect(bush_index)

def bush_edit(request, bush_id):
    """Изменить куст"""
    context = {}
    try:
        context['messages'] = request.session['messages']
        request.session.pop('messages')
    except KeyError:
        pass
    if request.method == 'POST':
        bush = get_object_or_404(Bush, pk=bush_id)
        form = BushFormForEdit(request.POST, instance=bush)
        if form.is_valid():
            form.save()
            context['messages'] = "Куст с id {0} по имени {1} изменен.".format(bush.id, bush.name)
            context['bush'] = get_object_or_404(Bush, pk=bush_id)
            context['form'] = BushFormForEdit(instance=bush)
            return render(request, 'firstapp/edit_bush.html', context=context)
        else:
            context['messages'] = form.errors
            return render(request, 'firstapp/edit_bush.html', context=context)
    else:
        bush = get_object_or_404(Bush, pk=bush_id)
        context['bush'] = bush
        context['form'] = BushFormForEdit(instance=bush)
        return  render(request, 'firstapp/edit_bush.html', context=context)


def remote_bug(request, bug_id):
    """Удаление жука"""
    bug = get_object_or_404(Bug, pk=bug_id)
    bug.delete()
    request.session['messages'] = "Жук ID: {0} с именем {1} удален".format(bug.id, bug.name)
    return redirect(request.META.get('HTTP_REFERER'))


def remote_bush(request, bush_id):
    """Удалить куст"""
    bush = get_object_or_404(Bush, pk=bush_id)
    bush.delete()
    request.session['messages'] = "Куст ID: {0} с именем {1} удален".format(bush_id, bush.name)
    return redirect(request.META.get('HTTP_REFERER'))


def search(request):
    """Выдает запрос поиска жука по имени"""
    context = {}
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_query = search_form.cleaned_data['name']
            query = Bug.objects.filter(name__contains=search_query).order_by('population')
            context['query'] = query
            test_query = Bush.objects.annotate().get()
        return render(request, 'firstapp/search.html', context=context)
    else:
        return render(request, 'firstapp/search.html', context=context)
