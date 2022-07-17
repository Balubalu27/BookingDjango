from django.contrib import admin
from table_booking.models import Table, TypeTable, Guest


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'price', 'seats_number')
    ordering = ('id', )


@admin.register(TypeTable)
class TypeTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_type')
    ordering = ('id', )


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'e_mail', 'phone_number', 'table')
    ordering = ('id', )
