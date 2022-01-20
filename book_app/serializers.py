from rest_framework import serializers, status
from django.contrib.auth.models import User
from .models import Office, Cabinet, Workplace, Booking

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        fields = ("id", "username", "password",)


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Office


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Cabinet


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Workplace


class BookingSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='username'
    # )

    class Meta:
        fields = '__all__'
        model = Booking

    booker = serializers.SlugRelatedField(slug_field='username', read_only=True)

    def create(self, data):
        """Функция создания бронирования с проверкой на незанятость."""
        datetime_from = data['datetime_from']
        datetime_to = data['datetime_to']
        workplace = data['workplace']
        # if date_from >= date_to:
        #     raise serializers.ValidationError(code=status.HTTP_400_BAD_REQUEST)
        # booked_1 = Booking.objects.select_related().filter(
        #     Q(date_from__range=(date_from, date_to)) | Q(
        #         date_to__range=(date_to, date_to)), office=office)
        # booked_2 = Booking.objects.select_related().filter(
        #     date_from__lte=date_from, date_to__gte=date_to, office=office)
        # booked_3 = Booking.objects.select_related().filter(
        #     date_from__lte=date_to,
        #     date_to__gte=date_from, office=office)

        booked = Booking.objects.filter(datetime_from__lt=datetime_to,
                                        datetime_to__gt=datetime_from,
                                        workplace=workplace).exists()

        # booked = booked_1.exists() | booked_2.exists() | booked_3.exists()
        if datetime_from >= datetime_to or booked:
            raise serializers.ValidationError(code=status.HTTP_400_BAD_REQUEST)
        return Booking.objects.create(**data)

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = '__all__'
#         model = User
