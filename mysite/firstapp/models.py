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


class Forest(models.Model):
    """Класс лес для  показа модели отношение один ко многим"""
    name = models.CharField(max_length=15, help_text="Имя леса", verbose_name='Имя')


class Tree(models.Model):
    """Класс дерево, показать отношнение один ко многим"""
    forest = models.ForeignKey(Forest, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, help_text='Название дерева', verbose_name='Название дерева')
    height = models.IntegerField()


class Bug(models.Model):
    """Клас Жук, показать отношение многие ко многим"""
    name = models.CharField(max_length=15, verbose_name='Название жука')
    population = models.IntegerField(verbose_name='Популяция')
    class Meta:
        ordering =['population']


class Bush(models.Model):
    """Модель куст, отношение многи ко многим"""
    name = models.CharField(max_length=15, verbose_name='Название куста')
    bugs = models.ManyToManyField(Bug)

    class Meta:
        ordering = ['name']


class Moss(models.Model):
    """Модель животное показать связь один к одному"""
    name = models.CharField(verbose_name='Имя', max_length=15)


class TypeMoss(models.Model):
    """Модель тип мха для отношение один к одному """
    type_moss = models.CharField(verbose_name='Тип мха', max_length=15)
    moss = models.OneToOneField(Moss, on_delete=models.CASCADE, primary_key=True)