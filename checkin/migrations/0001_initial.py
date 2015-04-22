# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('cpf', models.CharField(help_text=b'Apenas n\xc3\xbameros.', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='workshops',
            field=models.ManyToManyField(related_name='participants', to='checkin.Workshop', blank=True),
        ),
    ]
