from django.db import models
from django.utils import timezone


class Post(model.Model):
    nome = models.CharField(label='Nome', max_length=100)
    assunto = models.CharField(label='Assunto', max_length=100)
    email = models.EmailField(label='E-mail', max_length=100)
    mensagem = models.TextField(label='Mensagem')
    data_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.assunto
