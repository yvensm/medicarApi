from rest_framework.response import Response
from .serializers import ConsultaListSerializer, ConsultaStoreSerializer
from datetime import date
from django.db.models import Prefetch
from .models import Consulta
from rest_framework import serializers, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ConsultaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Consulta.objects.all()

    def list(self, request):
        data = Consulta.objects.filter(
            usuario__username=request.user).order_by('dia')
        serializer = ConsultaListSerializer(data, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ConsultaStoreSerializer(
            data=request.data, context={"req": request})
        data = {}
        if serializer.is_valid():
            consulta = serializer.save()
            data = consulta
        else:
            data = serializer.errors

        return Response(data)
