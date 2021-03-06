# Generated by Django 3.1 on 2020-08-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
