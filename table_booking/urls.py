from django.urls import path
from table_booking.views import TableAPIView


urlpatterns = [
    path('booking/', TableAPIView.as_view(), name='table_api'),
]
