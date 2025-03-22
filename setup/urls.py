from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_noticias import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Apps principais
    path('', include('app_home.urls'), name='home'),
    
    # Notícias e eventos
    path('noticias/', views.lista_noticias, name='lista_noticias'),
    path('noticia/<int:noticia_id>/', views.ler_noticia, name='ler_noticia'),
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('evento/<int:evento_id>/', views.ler_evento, name='ler_evento'),
    
    # Comunicados
    path('comunicados/', views.lista_comunicados, name='lista_comunicados'),
    path('comunicado/<int:comunicado_id>/', views.ler_comunicado, name='ler_comunicado'),
    
    # Outros aplicativos
    path('cadastro/', include('cadastro.urls')), 
    path('servicos/', include('app_atividade.urls')),
    path('atividade/', include('app_atividade.urls')), 
    

    # path("chat/", include("chat.urls")),
]

# Configuração para servir arquivos de mídia no modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
