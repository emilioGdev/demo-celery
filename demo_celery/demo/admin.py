from django.contrib import admin
from .models import Demo

@admin.register(Demo)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('message', 'level', 'created_at')
    list_filter = ('level', 'created_at')
    search_fields = ('message',)
