from django import forms


class Comentarios(forms.Form):
  
    nome = forms.CharField(label='Nome e Sobrenome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
