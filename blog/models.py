from django.db import models
from django.utils import timezone


class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    assunto = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField(max_length=1000)
    data_post = models.DateTimeField(default=timezone.now)

class Envio(models.Model):
    envioId = models.AutoField(primary_key=True)
    nomesobrenome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    mensagem = models.CharField(max_length=1000)

