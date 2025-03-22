from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'email', 'conteudo']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Seu email'}),
            'conteudo': forms.Textarea(attrs={'placeholder': 'Escreva seu comentário...', 'rows': 3}),
        }