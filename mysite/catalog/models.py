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
                                    verbose_name='Автор книги')
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
        return reverse('book-detail', args=[str(self.id)])

    # Показывает авторов кторыий писали книгу в в виде строки через запятую
    def display_author(self):
        authors = self.author.all()
        return ', '.join([author.last_name for author in authors])

    # Добавляет заголовок в таблицу админке
    display_author.short_description = 'Авторы'


class Status(models.Model):
    """Статус экземпляра книги"""
    name = models.CharField(max_length=20,
                            help_text='Введите статус книги',
                            verbose_name='Статус экземпляра')

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    """Отображает состояние экземпляра книги"""
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True,
                             verbose_name='Книга')
    inv_nom = models.CharField(max_length=20, null=True,
                               help_text='Ввведите инвентаризационный номер',
                               verbose_name='Инвентаризационный номер')
    imprint = models.CharField(max_length=200, null=True,
                               help_text='Введите издательство и год выпуска',
                               verbose_name='Издательство')
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True,
                               help_text='Изменить статус экземпляра книги',
                               verbose_name='Статус экземпляра книги')
    due_back = models.DateField(null=True, blank=True,
                                help_text='Введите окончание срока статуса',
                                verbose_name='Дата окончания статуса')

    def __str__(self):
        return '%s %s %s ' % (self.inv_nom, self.book, self.status)

    class Meta:
        ordering = ['due_back']
