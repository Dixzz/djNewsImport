from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import NewsModel
from datetime import datetime


class BookResource(resources.ModelResource):
    format = '%B, %d %Y %H:%M:%S'

    def before_import_row(self, row, **kwargs):
        dateStr = row['published']

        if dateStr:
            date = datetime.strptime(dateStr, self.format)
            row['published'] = date

    class Meta:
        model = NewsModel
        import_id_fields = ('title',)


@admin.register(NewsModel)
class BookAdmin(ImportExportModelAdmin):
    import_error_display = ("traceback",)
    resource_classes = [BookResource]
