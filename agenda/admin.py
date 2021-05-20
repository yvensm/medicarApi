from django.contrib import admin
from .models import Horario, Agenda
# Register your models here.


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('dia', 'medico')


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('hora', 'agenda', 'agendado')
