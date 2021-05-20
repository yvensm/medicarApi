from django.core.exceptions import ObjectDoesNotExist, ValidationError
from medicos.models import Medico
from agenda.serializers import HorarioListSerializer
from medicos.serializers import MedicoListSerializer
from django.db.models import fields
from rest_framework import serializers
from .models import Consulta
from datetime import datetime, date
from agenda.models import Agenda, Horario


class ConsultaListSerializer(serializers.ModelSerializer):
    medico = MedicoListSerializer(many=False, read_only=True)
    horario = HorarioListSerializer(many=False, read_only=True)

    class Meta:
        model = Consulta
        fields = ('data_agendamento', 'id', 'horario', 'medico', 'dia')


class ConsultaStoreSerializer(serializers.Serializer):
    agenda_id = serializers.IntegerField()
    horario = serializers.TimeField()

    def validate(self, data):
        def validate_hora(data):
            try:
                Horario.objects.get(
                    agenda__id=data['agenda_id'], hora=data['horario'], agendado=False)
            except ObjectDoesNotExist:
                raise ValidationError(
                    {'horario': 'Esse horário não está mais disponível'})

        def validate_dia(data):
            try:
                agenda = Agenda.objects.get(pk=data['agenda_id'])
                usuario = self.context["req"].user

                Consulta.objects.get(
                    dia=agenda.dia, usuario=usuario, horario__hora=data['horario'])
                raise ValidationError(
                    {'consulta': 'Você ja possui uma cunsulta marcada para este dia e horario'})
            except ObjectDoesNotExist:
                raise None
        validate_hora(data)
        validate_dia(data)

        return data

    def save(self):
        agenda_id = self.validated_data['agenda_id']
        horario = self.validated_data['horario']

        agenda = Agenda.objects.get(id=agenda_id)

        horario = Horario.objects.get(
            agenda__id=agenda_id, hora=horario, agendado=False)

        # return agenda
        medico = agenda.medico

        usuario = self.context["req"].user

        consulta = Consulta(dia=agenda.dia, horario=horario,
                            medico=medico, usuario=usuario)
        Horario.objects.filter(pk=horario.id).update(agendado=True)
        consulta.save()
        return ConsultaListSerializer(consulta).data
