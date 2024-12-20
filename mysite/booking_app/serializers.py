from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = authenticate()
        fields = ('username', 'email', 'password',)

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            "user": {
                "username": instance.username,
                "email": instance.email,
            },
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class RoomListSerializer(serializers.ModelSerializer):
    room_image = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'room_number','room_image', 'room_type', 'room_status', 'room_price']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_image = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_image', 'room_type', 'room_status', 'room_price',
                  'all_inclusive', 'room_description']


class ReviewSerializer(serializers.ModelSerializer):
    user_name = UserProfileSimpleSerializer()

    class Meta:
        model = Review
        fields = ['user_name', 'text', 'parent', 'stars']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    get_count_people =serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_image', 'address', 'hotel_stars', 'avg_rating', 'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class CountryDetailSerializer(serializers.ModelSerializer):
    hotels = HotelListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_name', 'hotels']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    country = CountrySerializer()
    owner = UserProfileSimpleSerializer()
    created_date = serializers.DateField(format('%d-%m-%Y'))
    rooms = RoomListSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_description','country', 'city',
                  'hotel_stars', 'hotel_image', 'hotel_video', 'created_date', 'address','owner', 'rooms', 'reviews']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
