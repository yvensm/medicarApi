from django.db import models
from especialidades.models import Especialidade


class Medico(models.Model):
    nome = models.CharField(max_length=255)
    crm = models.IntegerField(unique=True)
    email = models.EmailField(
        max_length=100, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=13, null=True, unique=True)
    especialidade = models.ForeignKey(
        Especialidade, related_name='especialidade', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

    def __str__(self):
        return self.nome
