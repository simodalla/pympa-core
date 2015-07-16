# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models import Organization, Office
from .forms import OrganizationAdminForm, OfficeAdminForm


RANGE_VALIDITA_SECTION = ('Range di validità',
                          {'fields': ('validity_start', 'validity_end'),
                           'classes': ('collapse',),}
                          )


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'parent')}),
        RANGE_VALIDITA_SECTION)
    list_display = ('title', 'parent')
    form = OrganizationAdminForm
    
    def get_form(self, request, obj=None, **kwargs):
        super(OrganizationAdmin, self).get_form(request, obj, **kwargs)


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'verbose_address')
    fieldsets = (
        (None, {'fields': ('title', 'organization', 'verbose_address')}),
        RANGE_VALIDITA_SECTION)
    form = OfficeAdminForm


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Office, OfficeAdmin)
