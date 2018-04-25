from django.conf.urls import url
from django.contrib.auth import views
from polls.views import *

app_name = 'polls'

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^registerstudent', CriarAluno.as_view(), name="registerstudent"),
    url(r'^registerbook', CriarLivro.as_view(), name="registerbook"),
    url(r'^registerlibrarian', CriarBlibliotecario.as_view(), name="registerlibrarian"),
    url(r'^contact', contact, name="contact"),
    url(r'^collection', collection, name="collection"),
    url(r'login', views.login, { 'template_name' : 'login.html' }, name="login"),
    url(r'logout_view', views.logout_then_login, { 'login_url' : '/login/' }, name="logout"),
]