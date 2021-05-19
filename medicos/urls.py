from django.urls import path
from .views import MedicoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', MedicoViewSet)

urlpatterns = [

]
