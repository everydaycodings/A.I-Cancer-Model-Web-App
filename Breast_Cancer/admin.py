from django.contrib import admin
from .models import Data
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Data)
class Add_friendAdmin(ImportExportModelAdmin):
   list_display = ("clump_thickness", "result")
   list_filter = ("result",)