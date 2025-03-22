from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia, Evento, Comunicado, Comentario
from .forms import ComentarioForm



def ler_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    comentarios = noticia.comentarios.order_by('-data_criacao')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = noticia
            comentario.save()
            return redirect('ler_noticia', noticia_id=noticia.id)
    else:
        form = ComentarioForm()

    return render(request, "pressa/ler_actualidade.html", {
        "noticia": noticia,
        "comentarios": comentarios,
        "form": form,
    })




def lista_noticias(request):
    noticias = Noticia.objects.order_by('-data_publicacao')
    if noticias.exists():
        return render(request, 'pressa/actualidade.html', {'noticias': noticias})
    else:
        return render(request, 'pressa/vazia.html')






def ler_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, "pressa/ler_evento.html", {"evento": evento})

def lista_comunicados(request):
    comunicados = Comunicado.objects.order_by('-data_publicacao')
    if comunicados.exists():
        return render(request, 'pressa/comunicado.html', {'comunicados': comunicados})
    else:
        return render(request, 'pressa/vazia.html')



def ler_comunicado(request, comunicado_id):
    comunicado = get_object_or_404(Comunicado, id=comunicado_id)
    return render(request, "pressa/ler_comunicado.html", {"comunicado": comunicado})




def lista_eventos(request):
    eventos = Evento.objects.all().order_by('data')
    if eventos.exists():
       return render(request, 'pressa/evento.html', {'eventos': eventos})
    else:
        return render(request, 'pressa/vazia.html')
    
