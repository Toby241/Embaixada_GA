# admin.py
from django.urls import path

from django.contrib import admin
from .models import MeuModelo  # Importando o modelo

class MeuModeloAdmin(admin.ModelAdmin):
    change_list_template = "admin/my_model_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('ir-para-dashboard/', self.redirect_dashboard),
        ]
        return custom_urls + urls

    def redirect_dashboard(self, request):
        # Coloque o link para o seu dashboard aqui
        return redirect("https://app.smartsupp.com/app/dashboard/conversations/coZW8OTEUPVmg")

admin.site.register(MeuModelo, MeuModeloAdmin)  # Registrando o modelo
