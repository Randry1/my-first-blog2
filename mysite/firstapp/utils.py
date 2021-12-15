import os
import threading
import time
import posixpath

from django.db.models import F
from django.shortcuts import render

from .forms import UpdatePerson
from .models import Person


def update_post(request, persons, form, template, title, messages):
    """Функция для обновления данных в модели"""
    if request.method == 'POST':
        form = UpdatePerson(request.POST)
        if form.is_valid():
            id_person = int(form.cleaned_data['id_person'])
            name = str(form.cleaned_data['name'])
            bio = str(form.cleaned_data['bio'])
            person = Person.objects.filter(id=id_person).update(name=name, bio=bio)
            return render(request, template,
                          context={"title": title, "header": title, "form": form, "messages": messages,
                                   "persons": persons})
        else:
            return render(request, template,
                          context={"title": title, "header": title, "form": form, "messages": messages,
                                   "persons": persons})
    else:
        return render(request, template,
                      context={"title": title, "header": title, "form": form, "messages": messages, "persons": persons})


def update_post_f(request, persons, form, template, title, messages):
    """Функция для обновления данных в модели"""
    if request.method == 'POST':
        form = UpdatePerson(request.POST)
        if form.is_valid():
            id_person = int(form.cleaned_data['id_person'])
            name = str(form.cleaned_data['name'])
            age = int(form.cleaned_data['age'])
            bio = str(form.cleaned_data['bio'])
            persons = Person.objects.filter(age=age)
            persons.update(name=name, bio=bio, age=F('age')+1)
            persons = Person.objects.filter(age=age+1)
            messages = 'Были обновлены'
            return render(request, template,
                          context={"title": title, "header": title, "form": form, "messages": messages,
                                   "persons": persons})
        else:
            return render(request, template,
                          context={"title": title, "header": title, "form": form, "messages": messages,
                                   "persons": persons})
    else:
        return render(request, template,
                      context={"title": title, "header": title, "form": form, "messages": messages, "persons": persons})


def update_post_update_or_create(request, persons, form, template, title, messages):
    """Функция для обновления данных в модели"""
    if request.method == 'POST':
        form = UpdatePerson(request.POST)
        if form.is_valid():
            id_person = int(form.cleaned_data['id_person'])
            name = str(form.cleaned_data['name'])
            age = int(form.cleaned_data['age'])
            bio = str(form.cleaned_data['bio'])
            data_for_defaults_person = {"name":name, "age":age, "bio":bio}
            person, created = Person.objects.update_or_create(id=id_person, defaults=data_for_defaults_person)
            if created == True:
                messages = 'Записи нет в базе данных, персона была добаленеа'
            return render(request, template,
                          context={"title": title, "header": title, "form": form, "messages": messages,
                                   "persons": persons})
        else:
            return render(request, template,
                          context={"title": title, "header": title, "form": form, "messages": messages,
                                   "persons": persons})
    else:
        return render(request, template,
                      context={"title": title, "header": title, "form": form, "messages": messages, "persons": persons})