from datetime import date, datetime, time
from agenda.serializers import AgendaListSerializer, AgendaSerializer
from django.db.models import Prefetch
from .models import Horario, Agenda
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AgendaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Agenda.objects.prefetch_related(
        Prefetch
        ('horarios',
         queryset=Horario.objects.all().filter(agendado=False, hora__gte=datetime.now().time()).order_by('hora'))
    ).filter(dia__gte=date.today()).order_by('dia')

    serializer_class = AgendaSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['medico']
    filterset_fields = ['medico']

    def get_serializer_class(self):
        if(self.action == 'list'):
            return AgendaListSerializer
        return super().get_serializer_class()
