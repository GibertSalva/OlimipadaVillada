# Generated by Django 2.2 on 2021-08-20 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Detector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='sensor_egreso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Detector.Sensor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='sensor_ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sucursal_requests_created', to='Detector.Sensor'),
        ),
    ]