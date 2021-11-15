from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from advertisement.models import AppPerformance


class AppPerformanceResource(resources.ModelResource):
    class Meta:
        model = AppPerformance


class AppPerformanceAdmin(ImportExportModelAdmin):
    resource_class = AppPerformanceResource


admin.site.register(AppPerformance, AppPerformanceAdmin)
