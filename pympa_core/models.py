# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .managers import ValidityDateTimeRangeManager


class ValidityDateTimeRangeModel(models.Model):
    validity_start = models.DateTimeField(
        verbose_name=_('data inizio validita'), default=timezone.now)
    validity_end = models.DateTimeField(
        verbose_name=_('data fine validita'), blank=True, null=True)

    objects = ValidityDateTimeRangeManager()

    class Meta:
        abstract = True

    def is_valido(self):
        from django.utils.timezone import now
        if self.validity_start <= now() and (
                not self.validity_end or self.validity_end >= now()):
            return True
        return False


@python_2_unicode_compatible
class Organization(TimeStampedModel, ValidityDateTimeRangeModel):
    """Ente"""
    title = models.CharField(max_length=200, unique=True,
                             verbose_name=_('title'))
    parent = models.ForeignKey('self', blank=True, null=True,
                               verbose_name=_('parent organization'))

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def __str__(self):
        return '{}'.format(self.title)


@python_2_unicode_compatible
class Office(TimeStampedModel, ValidityDateTimeRangeModel):
    """Sede"""
    title = models.CharField(max_length=200, unique=True)
    organization = models.ForeignKey(Organization)
    verbose_address = models.TextField(blank=True,
                                       verbose_name='verbose address')

    class Meta:
        verbose_name = _('Sede')
        verbose_name_plural = _('Sedi')

    def __str__(self):
        return '{}'.format(self.title)