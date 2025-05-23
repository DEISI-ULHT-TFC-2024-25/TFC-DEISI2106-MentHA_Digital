# Generated by Django 4.0.5 on 2022-11-29 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0006_grupocare_nivelgds_grupocare_programa'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GrupoCare',
            new_name='Grupo',
        ),
        migrations.RemoveField(
            model_name='grupoavalia',
            name='avaliador',
        ),
        migrations.RemoveField(
            model_name='grupoavalia',
            name='participante',
        ),
        migrations.DeleteModel(
            name='GrupoCog',
        ),
        migrations.RenameField(
            model_name='cuidador',
            old_name='grupoCare',
            new_name='grupo',
        ),
        migrations.RenameField(
            model_name='dinamizadorconvidado',
            old_name='grupoCare',
            new_name='grupo',
        ),
        migrations.RenameField(
            model_name='mentor',
            old_name='grupoCare',
            new_name='grupo',
        ),
        migrations.DeleteModel(
            name='GrupoAvalia',
        ),
    ]
