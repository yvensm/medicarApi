from globals.pagination import GlobalPagination
from rest_framework import serializers, viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Especialidade
from .serializers import EspecialidadeSerializer
from rest_framework.permissions import IsAuthenticated


class EspecialidadeViewSet(viewsets.ModelViewSet):
    """
    Especialidades
    """
    permission_classes = [IsAuthenticated]
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nome']
    pagination_class = GlobalPagination
