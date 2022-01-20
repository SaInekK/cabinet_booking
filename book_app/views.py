from datetime import datetime

import pytz
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Office, Cabinet, Workplace, Booking
from .permissions import IsOwnerAdminOrReadOnly, IsAuthorOrReadOnly
from .serializers import OfficeSerializer, CabinetSerializer, WorkplaceSerializer, BookingSerializer, UserSerializer


@api_view(['GET'])
def get_free_workplaces_view(request):
    """Returns workplaces that vacant in time interval datetime_from - datetime_to.
    Returns all workplaces if the parameters are not specified."""
    datetime_from = request.GET.get('datetime_from')
    datetime_to = request.GET.get('datetime_to')
    if not datetime_from or not datetime_to:
        workplaces = Workplace.objects.all()
        serializer = WorkplaceSerializer(workplaces, many=True)
        return Response(serializer.data)
    try:
        if datetime_from:
            datetime_from = datetime.strptime(datetime_from, '%Y-%m-%dT%H:%M')
        if datetime_to:
            datetime_to = datetime.strptime(datetime_to, '%Y-%m-%dT%H:%M')

        if datetime_from >= datetime_to:
            raise ValueError('Incorrect data.\nPlease enter date in "%Y-%m-%dT%H:%M" format.')
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # tz = pytz.timezone(settings.TIME_ZONE)
    # datetime_from = tz.localize(datetime_from)
    # datetime_to = tz.localize(datetime_to)

    bookings = Booking.objects.filter(datetime_from__lt=datetime_to,
                                      datetime_to__gt=datetime_from)
    workplaces_set = set(bookings.values_list('workplace', flat=True))
    workplaces = Workplace.objects.exclude(id__in=set(workplaces_set))
    serializer = WorkplaceSerializer(workplaces, many=True)
    return Response(serializer.data)


class BookingDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_bookings_by_workplace_id_view(request, pk=None):
    """Returns bookings by workplace id"""
    bookings = Booking.objects.filter(workplace__pk=pk)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_booking_view(request):
    """Booking workplace by id in datetime_from - datetime_to interval.
    Optional parameter: comment"""
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(booker=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
