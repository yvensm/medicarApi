from medicos.serializers import MedicoListSerializer
from rest_framework import serializers
from .models import Horario, Agenda
from datetime import datetime


class HorarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horario
        fields = ('hora', 'agenda', 'agendado',)


class HorarioListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horario
        fields = ('hora', 'agendado')

    def get_queryset(self):
        return Horario.objects.filter(agendado=False).order_by('hora')

    def to_representation(self, data):
        data = super(HorarioListSerializer, self).to_representation(data)
        hora = datetime.strptime(data['hora'], "%H:%M:%S")

        return hora.strftime("%H:%M")


class AgendaListSerializer(serializers.ModelSerializer):
    horarios = HorarioListSerializer(many=True, read_only=True)

    medico = MedicoListSerializer()

    class Meta:
        model = Agenda
        fields = ('id', 'dia', 'medico', 'horarios',)

    


class AgendaSerializer(serializers.ModelSerializer):
    horarios = HorarioSerializer(many=True)

    class Meta:
        model = Agenda
        fields = ('dia', 'medico', 'horarios',)

    def validate(self, data):
        return data
