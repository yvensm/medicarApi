from datetime import date, datetime, time
from functools import reduce
from agenda.serializers import AgendaListSerializer, AgendaSerializer
from django.db.models import Prefetch
from .models import Horario, Agenda
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Q
import operator
# import logging
# logger = logging.getLogger('app_api')


class AgendaFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filtro = {}
        especialidades = []
        for param in request.query_params:
            if(param == 'medico'):
                filtro['medico__pk'] = request.query_params['medico']
            if(param == 'especialidade'):
                especialidades = dict(request.GET)['especialidade']
            if(param == 'data_inicio'):
                filtro['dia__gte'] = request.query_params['data_inicio']
            if(param == 'data_final'):
                filtro['dia__lte'] = request.query_params['data_final']
        qset = queryset

        if(len(especialidades) > 0):
            list_of_Q = [Q(**{'medico__especialidade': val})
                         for val in especialidades]
            qset = qset.filter(reduce(operator.or_, list_of_Q))

        return qset.filter(**filtro)


class AgendaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Agenda.objects.prefetch_related(
        Prefetch
        ('horarios',
         queryset=Horario.objects.all().filter(agendado=False, hora__gte=datetime.now().time()).order_by('hora'))
    ).filter(dia__gte=date.today()).order_by('dia')

    serializer_class = AgendaSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # search_fields = ['medico']
    filterset_fields = []
    filter_backends = [AgendaFilter]

    def get_serializer_class(self):
        if(self.action == 'list'):
            return AgendaListSerializer
        return super().get_serializer_class()
