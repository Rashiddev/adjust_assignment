from django_filters import rest_framework as filters

from advertisement.models import AppPerformance


class AppPerformanceFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte')
    channel = filters.CharFilter(field_name='channel', lookup_expr='iexact')
    country = filters.CharFilter(field_name='country', lookup_expr='iexact')

    class Meta:
        model = AppPerformance
        fields = (
            'channel',
            'country',
            'os',
            'date'
        )
