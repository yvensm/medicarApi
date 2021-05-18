from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Especialidade
from .serializers import EspecialidadeSerializer
from rest_framework.permissions import IsAuthenticated

class EspecialidadeAPIView(APIView):
    """
    Especialidades
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        especialidades = Especialidade.objects.all()
        serializer = EspecialidadeSerializer(especialidades, many=True)
        return Response(serializer.data)
