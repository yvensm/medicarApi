from consultas.models import Consulta
from django.contrib import admin


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('dia', 'horario',
                    'data_agendamento', 'medico', 'usuario')
