from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    manufacturer = models.CharField('Марка', max_length=150)
    model = models.CharField('Модель', max_length=150)
    createYear = models.DateField('Год выпуска', null='false')
    power = models.IntegerField('Мощность', null='false')
    price = models.IntegerField('Цена', null='false')
    description = models.TextField('Описание', null='true')
    photo = models.ImageField(verbose_name='Изображения',
                              upload_to='photos/cars/', blank=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_start = models.DateTimeField(auto_now_add=False, verbose_name='Дата начала аренды')
    date_finish = models.DateTimeField(auto_now_add=False, verbose_name='Дата окончания аренды')
    createDate = models.DateTimeField(default=datetime.now(), verbose_name='Дата заявки')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ №{self.id} от {self.createDate.strftime('%d.%m.%Y %H:%M')}"
