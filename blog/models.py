from django.db import models
from django.utils import timezone


class Post(model.Model):
    nome = forms.CharField(label='Nome', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    data_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.assunto
