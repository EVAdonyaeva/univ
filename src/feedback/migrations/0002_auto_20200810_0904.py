# Generated by Django 3.0.8 on 2020-08-10 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 9, 4, 4, 374139)),
        ),
    ]
