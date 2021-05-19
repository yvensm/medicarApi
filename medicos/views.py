from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from .models import Medico
from .serializers import MedicoSerializer, MedicoListSerializer
from rest_framework.permissions import IsAuthenticated


class MedicoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nome', 'crm']
    filterset_fields = ['especialidade']

    def get_serializer_class(self):
        if(self.action == 'list'):
            return MedicoListSerializer
        return super().get_serializer_class()
