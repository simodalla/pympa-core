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
            name='Office',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('validity_start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='validity start')),
                ('validity_end', models.DateTimeField(blank=True, verbose_name='validity end', null=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('verbose_address', models.TextField(blank=True, verbose_name='verbose address')),
            ],
            options={
                'verbose_name_plural': 'offices',
                'verbose_name': 'office',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('validity_start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='validity start')),
                ('validity_end', models.DateTimeField(blank=True, verbose_name='validity end', null=True)),
                ('title', models.CharField(unique=True, verbose_name='title', max_length=200)),
                ('parent', models.ForeignKey(blank=True, verbose_name='parent organization', to='pympa_core.Organization', null=True)),
            ],
            options={
                'verbose_name_plural': 'organizations',
                'verbose_name': 'organization',
            },
        ),
        migrations.AddField(
            model_name='office',
            name='organization',
            field=models.ForeignKey(to='pympa_core.Organization'),
        ),
    ]
