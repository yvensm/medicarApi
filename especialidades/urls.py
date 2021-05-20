from .views import EspecialidadeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', EspecialidadeViewSet)

urlpatterns = [

]
