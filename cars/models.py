from django.db import models


# Create your models here.
class Car(models.Model):
    manufacturer = models.CharField(verbose_name='Марка',
                                    max_length=150)
    model = models.CharField(verbose_name='Модель',
                             max_length=150)
