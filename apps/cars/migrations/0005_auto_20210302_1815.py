# Generated by Django 3.1.7 on 2021-03-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20210302_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/cars/', verbose_name='Изображения'),
        ),
    ]
