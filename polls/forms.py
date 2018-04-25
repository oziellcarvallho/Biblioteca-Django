from django import forms
from django.contrib.auth.models import User

class CadastraEstudante(forms.Form):

    registration = forms.CharField(required=True)
    password_student = forms.CharField(required=True)

class CadastraBibliotecario(forms.Form):

    user = forms.CharField(required=True)
    password_librarian = forms.CharField(required=True)

class LoginForm(forms.Form):

    username = forms.CharField(required=True)
    senha = forms.CharField(required=True)

class CadastraUsuario(forms.Form):
    
    name_usr = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    cpf_usr = forms.CharField(required=True)
    phone = forms.CharField()
    cpf = forms.CharField(required=True)
    birth = forms.DateField(required=True)
    registration = forms.CharField(required=True)
    street = forms.CharField(required=True)
    num = forms.IntegerField(required=True)
    neighborhood = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state  = forms.CharField(required=True)

class CadastraLivro(forms.Form):
    
    name_book = forms.CharField(required=True)
    author_book = forms.CharField(required=True)
    subject_matter = forms.CharField(required=True)
    year = forms.IntegerField(required=True)
    edition = forms.CharField(required=True)
    publishing_company = forms.CharField(required=True)
