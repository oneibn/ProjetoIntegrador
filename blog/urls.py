from django.urls import path
from .views import  #Inserir nome das views criadas#


urlpatterns = [
    path('', index, name='index'),
    path('golpes/', golpes, name='golpes'),
    path('envio/', envio, name='envio'),
    path('dicas/', dicas, name='dicas'),
]
