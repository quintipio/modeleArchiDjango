# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPython', '0006_auto_20170518_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraceAppli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utilisateur', models.CharField(max_length=200)),
                ('heure', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(related_name='Categorie', to='blogPython.Categorie'),
        ),
    ]
