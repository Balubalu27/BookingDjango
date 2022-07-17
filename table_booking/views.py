from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from table_booking.models import Table, Guest
from table_booking.serializers import TableSerializer, TableCancelSerializer


class TableAPIView(ListAPIView):
    """Вывод всех столиков"""

    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDetailAPIView(RetrieveAPIView):
    """Информация о конкретном столике"""

    queryset = Table.objects.all()
    serializer_class = TableSerializer


class EditTableAPIView(RetrieveUpdateDestroyAPIView):
    """Представление для администратора с возможностью удаления/изменения/добавления записей,
    тут будет доп. permission только для admin"""

    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableSelectionAPIView(APIView):
    """
    Подбор столика.
    GET запрос - выведет все доступные на данный момент столики (не в блоке и не забронированные)
    POST - клиент вводит информацию (e-mail, номер телефона, имя) и выбирает столик.
    Информация записывается в таблицу Guest с которой работает учетная программа
    """
    def get(self, request):
        queryset = Table.objects.filter(is_closed_to_booking=False, is_booked=False)
        serializer = TableSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        В реквесте будет информация от пользователя, например из html формы,
        где будет указан e-mail, номер телефона и информация для фильтра по которой будут подобраны нужные столики.
        Информация о принятии заказа отправляется на указанный e-mail
        """
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            email_send()  # сюда будут передаваться параметры для отправки e-mail

            #  Записываем данные о пользователе в БД
            Guest.objects.create(
                name='Petr',
                e_mail='someemail@gmail.com',
                phone_number='349534957934',
                table=Table.objects.get(pk=1)
            )

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def email_send():
    """ Отправляет e-mail о принятии заказа"""

    subject = f'Бронирование столика'
    message = f'Заказ на бронирование столика принят, для отмены - перейдите по ссылке !!ТУТ БУДЕТ ССЫЛКА!!'
    from_email = 'balu.user961625@gmail.com'
    recipient_list = ['balushow123@gmail.com', ]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False
    )


class BookingCancelAPIView(RetrieveUpdateAPIView):
    """Отмена бронирования"""
    queryset = Table.objects.all()
    serializer_class = TableCancelSerializer
