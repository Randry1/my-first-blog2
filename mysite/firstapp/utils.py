import os
import threading
import time
import posixpath

from django.shortcuts import render

from .forms import UpdateColumnForm
from .models import Person


def update_post(request, persons, form, template, title, messages):
    """Функция для обновления данных в модели"""
    if request.method == 'POST':
        form = UpdateColumnForm(request.POST)
        if form.is_valid():
            delta_age = int(form.cleaned_data['delta_age'])
            person = Person.objects.filter(id=delta_age).update(name="Михаил")
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