from django.core.exceptions import FieldError
from django.db.models import Sum, F, OuterRef
from django_filters import rest_framework as d_filters
from rest_framework import filters, mixins, permissions, viewsets, status
from rest_framework.response import Response

from advertisement.api import serializers, filtersets

from advertisement.models import AppPerformance


class AppPerformanceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = AppPerformance.objects.all()
    serializer_class = serializers.AppPerformanceSerializer
    filter_backends = (d_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = filtersets.AppPerformanceFilter
    ordering_fields = (
        'date', 'channel', 'country', 'os', 'impressions',
        'clicks', 'installs', 'spend', 'revenue', 'cpi'
    )
    group_by_fields = ('date', 'channel', 'country', 'os')

    def get_serializer_context(self):
        context = super(AppPerformanceViewSet, self).get_serializer_context()
        context['group_by_fields'] = self.group_by_fields
        return context

    def list(self, request, *args, **kwargs):
        queryset = self.filter_backends[0]().filter_queryset(request, self.get_queryset(), self)

        group_by = request.GET.get('group_by')
        if group_by:
            try:
                queryset = queryset.values(*group_by.split(',')).annotate(
                    impressions=Sum('impressions'),
                    clicks=Sum('clicks'),
                    installs=Sum('installs'),
                    spend=Sum('spend'),
                    revenue=Sum('revenue'),
                ).annotate(cpi=F('spend')/F('installs')).order_by()
            except FieldError as e:
                abc = e
                import pdb;pdb.set_trace()
                return Response(f'group_by field should be from {self.group_by_fields}', status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = queryset.values()

        queryset = self.filter_backends[1]().filter_queryset(request, queryset, self)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
