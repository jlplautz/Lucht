from django.contrib import admin

from .models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'email',
        'cnh',
        'cpf',
        'data_nasc',
    )
    search_fields = ('nome',)
