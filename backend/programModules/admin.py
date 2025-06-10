from django.contrib import admin
from .models import programModules

@admin.register(programModules)
class programModule(admin.ModelAdmin):
    list_display = ('title','link','trainingProgram')
    search_fields = ('title',)

