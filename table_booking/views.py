from rest_framework.generics import ListAPIView

from table_booking.models import Table
from table_booking.serializers import TableSerializer


class TableAPIView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
