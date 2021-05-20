from functools import reduce
from globals.pagination import GlobalPagination
import operator
from django.db.models.query_utils import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from .models import Medico
from .serializers import MedicoSerializer, MedicoListSerializer
from rest_framework.permissions import IsAuthenticated


class MedicoFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filtro = {}
        especialidades = []
        for param in request.query_params:
            if(param == 'especialidade'):
                especialidades = dict(request.GET)['especialidade']
            if(param == 'search'):
                filtro['nome__contains'] = request.query_params['search']
        qset = queryset
        if(len(especialidades) > 0):
            list_of_Q = [Q(**{'especialidade': val})
                         for val in especialidades]
            qset = qset.filter(reduce(operator.or_, list_of_Q))
        return qset.filter(**filtro)


class MedicoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # search_fields = ['nome']
    # filterset_fields = ['especialidade']
    filter_backends = [MedicoFilter]
    pagination_class = GlobalPagination
    
    def get_serializer_class(self):
        if(self.action == 'list'):
            return MedicoListSerializer
        return super().get_serializer_class()
