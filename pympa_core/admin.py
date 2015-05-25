# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models import Organization, Office


RANGE_VALIDITA_SECTION = ('Range di validità',
                          {'fields': ('validity_start', 'validity_end')})


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'parent')}),
        RANGE_VALIDITA_SECTION)
    list_display = ('title', 'parent')


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'verbose_address')