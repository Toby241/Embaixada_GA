from django.urls import path
from .views import lista_noticias, ler_noticia, vazio
import views

urlpatterns = [
    path('', lista_noticias, name='lista_noticias'),
    path('<int:noticia_id>/', ler_noticia, name='ler_noticia'),
    path('eventos/', views.lista_eventos, name='lista_eventos'),
]
