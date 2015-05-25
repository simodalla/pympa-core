# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings


def admin_interface(request):
    # TODO: check if admin_interface key is already in context
    context = {'admin_interface': 'django.contrib.admin'}
    if 'grappelli' in settings.INSTALLED_APPS:
        context['admin_interface'] = 'grappelli'
    return context
