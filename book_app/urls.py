from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('workplaces/free/', get_free_workplaces_view, name='free_workplaces'),
    path('users/register/', CreateUserView.as_view(), name='create_user'),
    path('booking/by_id/<int:pk>/', get_bookings_by_workplace_id_view, name='get_bookings_by_workplace_id_view'),
    path('booking/detail/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('booking/create/', create_booking_view, name='booking_create'),
]


