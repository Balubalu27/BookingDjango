from django.db import models


class Table(models.Model):
    """Модель столика"""

    type = models.ForeignKey('TypeTable', verbose_name='Тип', on_delete=models.CASCADE)
    price = models.IntegerField('Стоимость столика')
    seats_number = models.IntegerField('Количество посадочных мест')
    is_booked = models.BooleanField('Забронирован', default=False)
    is_closed_to_booking = models.BooleanField('Заблокировать столик', default=False)

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'

    def __str__(self):
        return f'Тип: {self.type}, Цена: {self.price}, Мест: {self.seats_number}'


class TypeTable(models.Model):
    """Тип столика"""

    table_type = models.CharField('Тип столика', max_length=50)

    class Meta:
        verbose_name = 'Тип столика'
        verbose_name_plural = 'Типы столиков'

    def __str__(self):
        return f'{self.table_type}'


class Guest(models.Model):
    """Модель гостя"""

    name = models.CharField('Имя', max_length=100)
    e_mail = models.EmailField('E-mail')
    phone_number = models.CharField('Номер телефона', max_length=25)
    table = models.ForeignKey('Table', verbose_name='Столик', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'

    def __str__(self):
        return f'{self.name}, столик: {self.table}'
