from django.urls import path
from .views import AuthViewSet


urlpatterns = [
    path('register/', AuthViewSet.as_view({'post': 'register'})),
    path('login/', AuthViewSet.as_view({'post': 'login'})),
    path('logout/', AuthViewSet.as_view({'post': 'logout'})),
]