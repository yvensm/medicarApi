from django.urls import path
from .views import GetAuthToken, UserAPIView

urlpatterns = [
    path('login', GetAuthToken.as_view(), name='Login'),
    path('', UserAPIView.as_view(), name="Users")
]
