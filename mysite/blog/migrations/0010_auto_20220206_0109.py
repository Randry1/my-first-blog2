# Generated by Django 2.2.4 on 2022-02-05 18:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220206_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 18, 9, 23, 730818, tzinfo=utc)),
        ),
    ]
