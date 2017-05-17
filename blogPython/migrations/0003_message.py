# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPython', '0002_utilisateur_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origine', models.CharField(max_length=100)),
                ('text', models.TextField(null=True)),
                ('sujet', models.CharField(max_length=150)),
            ],
        ),
    ]