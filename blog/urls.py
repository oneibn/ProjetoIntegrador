from django.urls import path
from .views import  index, comentarios, envio, dicas


urlpatterns = [
    path('', index, name='index'),
    path('comentarios/', comentarios, name='comentarios'),
    path('envio/', envio, name='envio'),
    path('dicas/', dicas, name='dicas'),
]
