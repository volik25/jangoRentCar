from django.db import models


class Car(models.Model):
    manufacturer = models.CharField('Марка', max_length=150)
    model = models.CharField('Модель', max_length=150)
    power = models.IntegerField('Мощность', null='false')
    price = models.IntegerField('Цена', null='false')
    description = models.TextField('Описание', null='true')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
