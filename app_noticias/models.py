from django.db import models
from django.contrib.auth.models import User


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
   # autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Comunicado(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='comunicados/', null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    #autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo



class Comentario(models.Model):
    noticia = models.ForeignKey('Noticia', on_delete=models.CASCADE, related_name='comentarios')
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário por {self.nome} em {self.noticia.titulo}"



class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateTimeField()
    local = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo