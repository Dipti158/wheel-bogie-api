from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import WheelSpecification, BogieChecksheet
import json

@admin.register(WheelSpecification)
class WheelSpecificationAdmin(admin.ModelAdmin):
    list_display = ['form_number', 'submitted_by', 'submitted_date', 'status', 'created_at']
    list_filter = ['status', 'submitted_date', 'created_at']
    search_fields = ['form_number', 'submitted_by']
    readonly_fields = ['created_at', 'updated_at', 'fields_formatted']
    date_hierarchy = 'submitted_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('form_number', 'submitted_by', 'submitted_date', 'status')
        }),
        ('Specification Data', {
            'fields': ('fields_formatted',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def fields_formatted(self, obj):
        """Display"""


