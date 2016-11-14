from django.contrib import admin
from .models import Registrado


class AdminRegistrado(admin.ModelAdmin):
    list_display = ["__unicode__", "nombre", "codigo_postal", "timestamp", "actualizado"]

    class Meta:
        model = Registrado

admin.site.register(Registrado, AdminRegistrado)