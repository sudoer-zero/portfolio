from django.contrib import admin
from .models import Logo, RandomImage


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'description',
        'star',
        'created_at',
    ]


@admin.register(RandomImage)
class RandomImageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_at'
    ]
