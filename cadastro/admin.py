from django.contrib import admin
from .models import Cadastro

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'etudiant')  # Campos exibidos na lista
    search_fields = ('nom', 'prenom', 'email')  # Campos pesquisáveis
    list_filter = ('etudiant',)  # Filtros laterais