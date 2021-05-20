from django.urls import path
from .views import ConsultaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', ConsultaViewSet)

urlpatterns = [

]
