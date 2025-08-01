from django.db import models
from django.utils import timezone
import json

class WheelSpecification(models.Model):
    
    """Model for wheel specification forms"""
    
    STATUSES = [
        ('SAVED', 'Saved'),
        ('SUBMITTED', 'Submitted'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    
    form_number = models.CharField(
        max_length=50, 
        unique=True, 
        help_text="Unique form identifier"
    )
    submitted_by = models.CharField(
        max_length=100,
        help_text="User who submitted the form"
    )
    submitted_date = models.DateTimeField(
        default=timezone.now,
        help_text="Date and time when form was submitted"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default='SAVED',
        help_text="Current status of the form"
    )
    
    # Wheel specification fields stored as JSON
    fields = models.JSONField(
        default=dict,
        help_text="Wheel specification data in JSON format"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # db_table = 'wheel_specifications'
        ordering = ['-created_at']
        verbose_name = 'Wheel Specification'

    
    def __str__(self):
        return f"{self.form_number} - {self.status}"
    


class BogieChecksheet(models.Model):
    """Model for bogie checksheet forms"""
    
    STATUSES = [
        ('SAVED', 'Saved'),
        ('SUBMITTED', 'Submitted'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    
    form_number = models.CharField(
        max_length=50, 
        unique=True
    )
    inspection_by = models.CharField(max_length=100)
    inspection_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default='SAVED'
    )
    
    # Bogie details
    bogie_details = models.JSONField(default=dict)
    bogie_checksheet = models.JSONField(default=dict)
    bmbc_checksheet = models.JSONField(default=dict)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # db_table = 'bogie_checksheets'
        ordering = ['-created_at']
        verbose_name = 'Bogie Checksheet'
       
    
    def __str__(self):
        return f"{self.form_number} - {self.status}"



