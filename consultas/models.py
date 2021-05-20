from django.db import models
from medicos.models import Medico
from users.models import User
from agenda.models import Horario
# Create your models here.


class Consulta(models.Model):
    dia = models.DateField()
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
