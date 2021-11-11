from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import Post


# Utilizei function class based views, talvez mudar para class based views

def index(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'index.html', context)


def envio(request):
    context = {
         
    }
    return render(request, 'envio.html', context)
  
  
def golpes(request):
    context = {
         
    }
    return render(request, 'golpes.html', context)
  
  
def dicas(request):
    context = {
         
    }
    return render(request, 'dicas.html', context)

