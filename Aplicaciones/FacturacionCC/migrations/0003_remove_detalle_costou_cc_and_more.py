# Generated by Django 4.2.7 on 2024-01-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacturacionCC', '0002_rename_origen_cc_tipo_dificultad_cc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalle',
            name='costou_cc',
        ),
        migrations.RemoveField(
            model_name='platillo',
            name='porciones_cc',
        ),
        migrations.AddField(
            model_name='detalle',
            name='descripcion_cc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='platillo',
            name='costou_cc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.RemoveField(
            model_name='detalle',
            name='platillo_cc',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='ingrediente_cc',
        ),
        migrations.AddField(
            model_name='detalle',
            name='platillo_cc',
            field=models.ManyToManyField(to='FacturacionCC.platillo'),
        ),
        migrations.AddField(
            model_name='receta',
            name='ingrediente_cc',
            field=models.ManyToManyField(to='FacturacionCC.ingrediente'),
        ),
    ]