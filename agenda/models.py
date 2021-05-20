import re
from django.core.exceptions import ValidationError
from django.db import models
from medicos.models import Medico
from datetime import date, datetime
# Create your models here.


class Agenda(models.Model):
    dia = models.DateField()
    medico = models.ForeignKey(
        Medico, on_delete=models.CASCADE, related_name="medico")

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
        unique_together = [['dia', 'medico']]

    def __str__(self):
        return f"{self.medico} - {self.dia}"

    def clean(self) -> None:
        if self.dia < date.today():
            raise ValidationError(
                {'message': "Não foi possivel criar agenda para esse dia."})
        return super().clean()


class Horario(models.Model):
    hora = models.TimeField()
    agenda = models.ForeignKey(
        Agenda, on_delete=models.CASCADE, related_name='horarios')
    agendado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Horário"
        verbose_name_plural = "Horários"
        unique_together = [['agenda', 'hora']]

    def __str__(self):
        return self.hora.strftime('%H:%M')

    def clean(self) -> None:
        if(self.agendado):
            raise ValidationError(
                {'message': "Horário já agendado"})
        if (self.agenda.dia == date.today() and self.hora < datetime.now().time()):
            raise ValidationError(
                {'message': "Esse horário não pode ser criado"})
        return super().clean()
