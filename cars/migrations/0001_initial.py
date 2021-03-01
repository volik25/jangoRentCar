# Generated by Django 3.1.7 on 2021-03-01 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=150, verbose_name='Марка')),
                ('model', models.CharField(max_length=150, verbose_name='Модель')),
                ('power', models.IntegerField(null='false', verbose_name='Мощность')),
                ('price', models.IntegerField(null='false', verbose_name='Цена')),
                ('description', models.TextField(null='true', verbose_name='Описание')),
            ],
        ),
    ]
