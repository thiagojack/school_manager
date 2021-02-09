from django.contrib import admin
from .models import Subject

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'school_year', 'teacher')
    list_filter = ('name', 'category', 'school_year', 'teacher')
    search_fields = ('name', 'category', 'school_year', 'teacher')
    list_editable = ('category', 'school_year')