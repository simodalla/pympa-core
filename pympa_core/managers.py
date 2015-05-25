# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db.models import Manager, Q
from django.utils.timezone import now


class ValidityDateTimeRangeManager(Manager):

    def valid(self):
        return self.filter(
            Q(validity_start__lte=now()),
            Q(validity_end__gte=now()) | Q(validity_end__isnull=True),)
