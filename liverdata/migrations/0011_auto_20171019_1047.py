# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liverdata', '0010_auto_20171018_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ire',
            name='device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liverdata.Device'),
        ),
        migrations.AlterField(
            model_name='lesion',
            name='lesiontype',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='liverdata.LesionType'),
        ),
        migrations.AlterField(
            model_name='mwa',
            name='device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liverdata.Device'),
        ),
        migrations.AlterField(
            model_name='rfa',
            name='device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liverdata.Device'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='treatmentname',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='liverdata.TreatmentName'),
        ),
    ]
