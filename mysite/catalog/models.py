from django.db import models


# Create your models here.
from django.urls import reverse


class Genre(models.Model):
    """Модель жанр для книг отношнение многие ко многим"""
    name = models.CharField(max_length=200,
                            help_text='Введите жанр книги',
                            verbose_name='Жанр книги')

    def __str__(self):
        return self.name


class Language(models.Model):
    """Модель Язык для книги указать язык на котором написана книга"""
    name = models.CharField(max_length=20,
                            help_text='Введите язык книги',
                            verbose_name='Язык книги')

    def __str__(self):
        return self.name


class Author(models.Model):
    """Модель Автор книги"""
    first_name = models.CharField(max_length=100,
                                  help_text='Ведите имя автора',
                                  verbose_name='Имя автора')
    last_name = models.CharField(max_length=100,
                                 help_text='Введите фамилию автора',
                                 verbose_name='Фамилия автора')
    date_of_birth = models.DateField(help_text='Введите дату рождения',
                                     verbose_name='Дата рождения',
                                     null=True, blank=True)
    date_of_death = models.DateField(help_text='Введите дату смерти если автор умер',
                                     verbose_name='Дата смерти',
                                     null=True, blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    """Клас Книга оин ко многим с жанром"""
    title = models.CharField(max_length=200,
                             help_text='Введите название книги',
                             verbose_name='Название книги')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              help_text='Выберете жанр книги',
                              verbose_name='Жанр книги',
                              null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 help_text='Выберете язык книги',
                                 verbose_name='Язык книги', null=True)
    author = models.ManyToManyField('Author', help_text='Выберете автора книги',
                                    verbose_name='Автор книги',
                                    null=True)
    summary = models.TextField(max_length=100,
                               help_text='Введите краткое описание',
                               verbose_name='Краткое описание книги')
    isbn = models.CharField(max_length=13,
                            help_text='Должно содержать 13 символов',
                            verbose_name='ISBN книги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #  Возвращает URL адрес экземпляра книги
        return reverse('bool-detail', args=[str(self.id)])