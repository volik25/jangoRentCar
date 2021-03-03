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
        return f"{self.id}: {self.manufacturer} {self.model}"


class Order(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateTimeField('Дата и время начала аренды')
    date_finish = models.DateTimeField('Дата и время окончания аренды')
    createDate = models.DateTimeField('Дата заявки', default=datetime.now())

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ №{self.id} от {self.createDate}"
