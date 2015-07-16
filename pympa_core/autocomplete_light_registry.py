# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

try:
    import autocomplete_light
    from .models import Organization

    class OrganizationAutocomplete(autocomplete_light.AutocompleteModelBase):
        search_fields = ['title',]
        model = Organization

    autocomplete_light.register(OrganizationAutocomplete)
except ImportError:
    pass
