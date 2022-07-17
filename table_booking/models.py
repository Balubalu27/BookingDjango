from django.db import models


class Table(models.Model):
    type = models.ForeignKey('TypeTable', verbose_name='Тип', on_delete=models.CASCADE)
    price = models.IntegerField('Стоимость столика')
    seats_number = models.IntegerField('Количество посадочных мест')
    is_booked = models.BooleanField('Состояние бронирования', default=False)
    is_closed_to_booking = models.BooleanField('Состояние блокирования бронирования', default=False)

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'

    def __str__(self):
        return f'Тип: {self.type}, Цена: {self.price}, Мест: {self.seats_number}'


class TypeTable(models.Model):
    table_type = models.CharField('Тип столика', max_length=50)

    class Meta:
        verbose_name = 'Тип столика'
        verbose_name_plural = 'Типы столиков'

    def __str__(self):
        return self.table_type
