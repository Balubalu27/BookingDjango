from django.contrib import admin
from table_booking.models import Table, TypeTable


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'price', 'seats_number')
    ordering = ('id', )


@admin.register(TypeTable)
class TypeTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_type')
    ordering = ('id', )

