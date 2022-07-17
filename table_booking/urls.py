from django.urls import path
from table_booking.views import TableAPIView, TableDetailAPIView, EditTableAPIView, TableSelectionAPIView, \
    BookingCancelAPIView

urlpatterns = [
    path('booking/', TableAPIView.as_view(), name='all_tables'),
    path('booking/<int:pk>/', TableDetailAPIView.as_view(), name='table_detail'),
    path('booking/admin/<int:pk>/', EditTableAPIView.as_view(), name='edit_table'),
    path('booking/select/', TableSelectionAPIView.as_view(), name='select'),
    path('booking/cancel/<int:pk>/', BookingCancelAPIView.as_view(), name='cancel'),

]
