# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.TextField()),
                ('dest', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
                ('dFrom', models.DateField()),
                ('dTo', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='login_registration.User')),
            ],
        ),
    ]