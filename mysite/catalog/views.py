from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from .models import Book, BookInstance, Author


def index(request):
    """index catalog book"""
    # Колличество книг и колличество экземпляров книг
    num_book = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()

    # Доступные книги, статус на складе
    num_instance_available = BookInstance.objects.filter(status__exact=2).count()
    # Авторы книг колличество
    # Здесь было .all() применено по умолчанию
    num_author = Author.objects.count()

    # отрисовка шаблона
    return render(request, 'catalog/index.html', context={
        'num_book': num_book,
        'num_instance': num_instance,
        'num_instance_available': num_instance_available,
        'num_author': num_author
    })
