
# admin.py
from django.contrib import admin
from .models import Noticia, Evento, Comunicado
from .models import Comentario


admin.site.register(Noticia)
admin.site.register(Comunicado)
admin.site.register(Evento)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'noticia', 'data_criacao', 'conteudo_preview')
    search_fields = ('nome', 'email', 'conteudo')
    list_filter = ('data_criacao', 'noticia')
    ordering = ('-data_criacao',)

    def conteudo_preview(self, obj):
        return obj.conteudo[:50] + "..." if len(obj.conteudo) > 50 else obj.conteudo

    conteudo_preview.short_description = 'Conteúdo'

    def delete_model(self, request, obj):
        # Exibe uma mensagem personalizada ao excluir
        self.message_user(request, f"O comentário de {obj.nome} foi excluído com sucesso.")
        super().delete_model(request, obj)


