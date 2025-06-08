from django.contrib import admin
from .models import Alert, Demo

@admin.register(Demo)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('message', 'level', 'created_at')
    list_filter = ('level', 'created_at')
    search_fields = ('message',)

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'category', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('message',)