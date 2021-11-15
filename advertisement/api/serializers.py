from rest_framework import serializers

from advertisement.api.mixins import QueryFieldsMixin
from advertisement.models import AppPerformance


class AppPerformanceSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    # cpi = serializers.SerializerMethodField()

    class Meta:
        model = AppPerformance
        fields = (
            'id',
            'date',
            'channel',
            'country',
            'os',
            'impressions',
            'clicks',
            'installs',
            'spend',
            'revenue',
            'cpi'
        )

    # def get_cpi(self, obj):
    #     return obj['spend']/obj['installs']
