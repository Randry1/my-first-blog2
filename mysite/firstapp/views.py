import os
from array import array
from os.path import normpath

from django.contrib.sessions.backends import file
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from .forms import UserForm, HelperTextContactForm, CharFieldForm, SlugFieldForm, UrlFieldForm, UuiFieldForm, \
    ComboFieldForm, FilePathFieldForm, FileFieldForm, DateFieldForm, TimeFieldForm, DateTimeFieldForm, WidgetForm, \
    ThinTinctureForm, UserBookForm, CreatePerson

# Create your views here.
from .models import Person


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
    content += '<a href="/firstapp/method_get_person/15/" class="btn btn-info">Функции модели</a><br> '
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
    except Person.MultipleObjectsReturned:  # Вызывает когда собподений больше одного
        second_person = {"name": 'Сильно много совпадений'}
    return render(request, 'firstapp/method_person.html',
                  context={"title": 'Методы модели', "first_person": first_person, "second_person": second_person})
