# Generated by Django 2.2.4 on 2021-12-15 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.CharField(default='', max_length=300),
        ),
    ]