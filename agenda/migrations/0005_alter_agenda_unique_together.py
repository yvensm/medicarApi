# Generated by Django 3.2.3 on 2021-05-20 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_alter_medico_especialidade'),
        ('agenda', '0004_alter_agenda_medico'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together={('dia', 'medico')},
        ),
    ]