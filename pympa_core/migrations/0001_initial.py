# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('inizio_validita', models.DateTimeField(verbose_name='Data inizio validita', default=django.utils.timezone.now)),
                ('fine_validita', models.DateTimeField(verbose_name='Data fine validita', null=True, blank=True)),
                ('titolo', models.CharField(max_length=200, unique=True)),
                ('ente_padre', models.ForeignKey(blank=True, to='pympa_core.Ente', null=True)),
            ],
            options={
                'verbose_name': 'Ente',
                'verbose_name_plural': 'Enti',
            },
            bases=(models.Model,),
        ),
    ]
