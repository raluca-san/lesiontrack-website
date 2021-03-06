# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liverdata', '0014_auto_20171020_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='TPErrors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lateralerror', models.CharField(max_length=500)),
                ('longerror', models.CharField(max_length=500)),
                ('angularerror', models.CharField(max_length=500)),
                ('residualerror', models.CharField(max_length=500)),
                ('trajectory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='liverdata.Trajectory')),
            ],
            options={
                'verbose_name_plural': 'TPErrors',
            },
        ),
        migrations.AlterModelOptions(
            name='lesion',
            options={'ordering': ['patient', 'lesion_nr']},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['patient_name', 'patient_name']},
        ),
        migrations.AlterModelOptions(
            name='treatmentsession',
            options={'ordering': ['treatment_type', 'treatmentsession_date']},
        ),
    ]
