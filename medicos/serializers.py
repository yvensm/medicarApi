from especialidades.serializers import EspecialidadeSerializer
from rest_framework import serializers
from .models import Medico


class MedicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = ('id', 'nome', 'crm', 'email', 'especialidade')


class MedicoListSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer(many=False, read_only=True)

    class Meta:
        model = Medico
        fields = ('id', 'nome', 'crm', 'email', 'especialidade')
