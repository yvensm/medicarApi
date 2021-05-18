from django.urls import path

from .views import EspecialidadeAPIView

urlpatterns = [
    path('', EspecialidadeAPIView.as_view(), name='especialidades')
]
