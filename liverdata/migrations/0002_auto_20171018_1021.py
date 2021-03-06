# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liverdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_name', models.TextField()),
                ('short_name', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterModelOptions(
            name='ire',
            options={'verbose_name_plural': 'IRE'},
        ),
        migrations.AlterModelOptions(
            name='mwa',
            options={'verbose_name_plural': 'MWA'},
        ),
        migrations.AlterModelOptions(
            name='rfa',
            options={'verbose_name_plural': 'RFA'},
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='treatment_name',
        ),
    ]
