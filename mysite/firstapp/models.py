from django.db import models

class Person(models.Model):
    """Первый раза использую БД глава из книжки"""
    name = models.CharField(max_length=12)
    age = models.IntegerField()
