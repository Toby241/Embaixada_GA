from django.urls import path

from .views import cadastrar,cadastro

urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
    path('cadastrar', cadastrar, name='cadastrar'),
    
]