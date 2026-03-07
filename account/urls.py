from django.urls import path, include
from account.views import LogoutView
from account.views import APIViewSet

urlpatterns = [
    path('auth/login', include('dj_rest_auth.urls'), name = 'login'),
    path('auth/register/', include('dj_rest_auth.registration.urls'), name= 'register'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]