from django.contrib import admin
from .models import Logo


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'description',
        'star',
        'created_at',
    ]
