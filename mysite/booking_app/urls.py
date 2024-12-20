from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import *
from django.conf.urls.i18n import i18n_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = SimpleRouter()
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'booking', BookingViewSet, basename='bookings')

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('en/register/', RegisterView.as_view(), name='register'),
    path('urls/', include(router.urls)),
    path('', HotelListAPIView.as_view(), name='hotel_list'),
    path('<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('rooms/', RoomListAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('rooms/create/', RoomCreateAPIView.as_view(), name='room_create'),
    path('rooms/create/<int:pk>/', RoomEDITAPIView.as_view(), name='room_edit'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('hotel/create/', HotelCreateAPIView.as_view(), name='hotel_create'),
    path('hotel/create/<int:pk>/', HotelEDITAPIView.as_view(), name='hotel_edit'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]