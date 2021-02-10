from apps.grids.models import Grid
from django.contrib import admin

# Register your models here.

@admin.register(Grid)
class GridAdmin(admin.ModelAdmin):
    list_display = ('student', 'subjects')