from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import Post, Envio

# Utilizei function class based views, talvez mudar para class based views

def index(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'index.html', context)

## Aqui a view recebe as informações do formulário por HttpPost, cria uma instância e salva a instância no banco de dados
def envio(request):
    if request.method == 'POST':
        nomesobrenome = request.POST['nomesobrenome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        mensagem = request.POST['mensagem']

        ins = Envio(nomesobrenome=nomesobrenome, email=email, telefone=telefone, mensagem=mensagem)
        ins.save()

    context = {
        'envio': Envio.objects.all()
    }
    return render(request, 'envio.html', context)
  
  
def comentarios(request):
    context = {
         
    }
    return render(request, 'comentarios.html', context)
  
  
def dicas(request):
    context = {
         
    }
    return render(request, 'dicas.html', context)

