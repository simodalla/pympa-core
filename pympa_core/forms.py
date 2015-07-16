# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .models import Organization, Office

try:
    from autocomplete_light import ModelForm as AutocompleteModelForm

    class OrganizationAdminForm(AutocompleteModelForm):
        class Meta:
            model = Organization
            autocomplete_fields = ('parent',)
            exclude = []

    class OfficeAdminForm(AutocompleteModelForm):
        class Meta:
            model = Office
            autocomplete_fields = ('organization',)
            exclude = []

except ImportError:

    from django.contrib import admin

    class OrganizationAdminForm(admin.ModelAdmin):
        class Meta:
            model = Organization
            exclude = []

    class OfficeAdminForm(admin.ModelAdmin):
        class Meta:
            model = Office
            exclude = []