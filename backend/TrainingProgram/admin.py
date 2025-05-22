from django.contrib import admin
from .models import TrainingProgram

@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'program_type', 'duration', 'start_date', 'end_date', 'status')
    search_fields = ('program_name',)
    list_filter = ('program_type', 'status', 'start_date', 'end_date')

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'certificate_number', 'offered_by', 'training_program')
    search_fields = ('name', 'certificate_number')
    list_filter = ('offered_by',)