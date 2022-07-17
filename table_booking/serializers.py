from rest_framework import serializers

from table_booking.models import Table


class TableSerializer(serializers.ModelSerializer):
    """Сериализирует все поля модели Table"""

    type = serializers.SlugRelatedField(slug_field='table_type', read_only=True)

    class Meta:
        model = Table
        fields = '__all__'


class TableCancelSerializer(serializers.ModelSerializer):
    """Сериализиет поле is_booked для отмены брони"""

    class Meta:
        model = Table
        fields = ('is_booked', )
