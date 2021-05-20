from agenda.models import Agenda
from django.urls import path
from .views import AgendaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', AgendaViewSet)

urlpatterns = [

]
