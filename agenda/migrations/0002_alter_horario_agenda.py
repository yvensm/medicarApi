# Generated by Django 3.2.3 on 2021-05-19 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='agenda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numeros', to='agenda.agenda'),
        ),
    ]
