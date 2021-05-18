from django.db import models


class Especialidade(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.nome
