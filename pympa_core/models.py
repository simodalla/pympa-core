# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from model_utils.models import TimeStampedModel

from .managers import RangeValiditaManager


class RangeValiditaModel(models.Model):
    inizio_validita = models.DateTimeField(verbose_name='Data inizio validita',
                                           default=timezone.now)
    fine_validita = models.DateTimeField(verbose_name='Data fine validita',
                                         blank=True, null=True)

    objects = RangeValiditaManager()

    class Meta:
        abstract = True

    def is_valido(self):
        from django.utils.timezone import now
        if self.inizio_validita <= now() and (
                not self.fine_validita or self.fine_validita >= now()):
            return True
        return False


@python_2_unicode_compatible
class Ente(TimeStampedModel, RangeValiditaModel):
    titolo = models.CharField(max_length=200, unique=True)
    ente_padre = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        verbose_name = 'Ente'
        verbose_name_plural = 'Enti'

    def __str__(self):
        return '{}'.format(self.titolo)