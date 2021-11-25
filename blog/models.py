from django.db import models
from django.utils import timezone


class Post(models.Model):
    nome = models.CharField(max_length=100)
    assunto = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField(max_length=1000)
    data_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.assunto
