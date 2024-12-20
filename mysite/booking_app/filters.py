import django_filters
from .models import Hotel, Room, Booking


class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'hotel_name': ['icontains'],
            'address': ['icontains'],
            'owner': ['exact'],
        }


class RoomFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_status': ['exact'],
            'hotel_room': ['exact'],
            'room_price': ['gte', 'lte'],
        }


class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = {
            'room_book': ['exact'],
            'user_book': ['exact'],
            'check_in': ['gte'],
            'check_out': ['lte'],
            'status_book': ['exact'],
        }
