from django.db import models


class Table(models.Model):
    type = models.ForeignKey('TypeTable', on_delete=models.CASCADE)
    price = models.IntegerField('Стоимость столика')
    seats_number = models.IntegerField('Количество посадочных мест столика')


class TypeTable(models.Model):
    simple = models.CharField('Обычный столик', max_length=50)
    cabin = models.CharField('Кабина', max_length=50)
    room = models.CharField('Комната', max_length=50)

