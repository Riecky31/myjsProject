from django.contrib import admin
from .models import Intern

@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'first_name', 'last_name', 'email', 'phone', 'gender', 'start_date', 'end_date')
    search_fields = ('first_name', 'last_name', 'email', 'id_number')
    list_filter = ('gender', 'start_date', 'end_date')

