from django.db import models

class Person(models.Model):
    """Первый раза использую БД глава из книжки"""
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    bio = models.CharField(max_length=300, default='')


class Electric(models.Model):
    """Модель электриков"""
    name = models.CharField(help_text='ФИО', max_length=15)
    dict = models.CharField(help_text='Район', blank=True, max_length=230)
    email = models.EmailField(blank=True)
    # avatar = models.ImageField(blank=True) #  Cannot use ImageField because Pillow is not installed. todo https://pypi.org/project/Pillow/
    bio = models.CharField(blank=True, help_text='О себе', max_length=230)
    active = models.BooleanField(default=True, help_text='Работает')

