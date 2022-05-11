from django_filters import rest_framework as filters

from .models import *


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TestFilter(filters.FilterSet):
    subjects = CharFilterInFilter(field_name='subject__title', lookup_expr='in')

    class Meta:
        model = Test
        fields = ['subject']  # filter by
