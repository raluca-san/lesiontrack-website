# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liverdata', '0005_treatment_treatmentname'),
    ]

    operations = [
        migrations.CreateModel(
            name='LesionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesiontype_name', models.CharField(max_length=50)),
                ('lesiontype_shortname', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesion',
            name='lesion_name',
        ),
    ]
