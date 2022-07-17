from rest_framework import serializers

from table_booking.models import Table


class TableSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='table_type', read_only=True)

    class Meta:
        model = Table
        fields = '__all__'
