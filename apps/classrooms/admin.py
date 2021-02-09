from apps.classrooms.models import Classroom
from django.contrib import admin
from .models import Classroom, SchoolYear

# Register your models here.
@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('school_year', 'identified', 'shift')
    list_filter = ('school_year', 'identified', 'shift')
    search_fields = ('school_year', 'shift')
    list_editable = ('identified', 'shift')
    raw_id_fields = ('school_year',)


@admin.register(SchoolYear)
class SchoolYearAdmin(admin.ModelAdmin):
    list_display = ('type', 'lective_year')
    list_filter = ('type', 'lective_year')
    search_fields = ('type', 'lective_year')