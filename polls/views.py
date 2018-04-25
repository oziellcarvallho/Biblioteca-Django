from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import *
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def collection(request):
    bl = Book.objects.all()
    return render(request, 'collection.html', {'bl': bl})

class CriarAluno(View):
    template_name = 'registerstudent.html'

    def get(self, request):
        return render(request, self.template_name)
        
    def post(self, request):
        form = CadastraUsuario(request.POST)
        dados_form = form.data
        
        form_aluno = CadastraEstudante(request.POST)
        dados_form_aluno = form_aluno.data

        usuario_auth = User.objects.create_user(dados_form_aluno['registration'], dados_form['email'], dados_form_aluno['password_student'])

        u = Usuario(name_usr=dados_form['name_usr'],
                    cpf_usr=dados_form['cpf_usr'],
                    email=dados_form['email'],
                    street=dados_form['street'],
                    number=dados_form['num'],
                    phone=dados_form['phone'],
                    postcard=dados_form['postcard'],
                    city=dados_form['city'],
                    state=dados_form['state'],
                    neighborhood=dados_form['neighborhood'],
                    birth=dados_form['birth'],
                    usuario=usuario_auth,
                    )
        u.save()
        
        u.student_set.create(registration=dados_form_aluno['registration'],
                                password_student=dados_form_aluno['password_student'],
                                )
         
        return render(request, self.template_name)

class CriarBlibliotecario(View):
    template_name = 'registerlibrarian.html'

    def get(self, request):
        return render(request, self.template_name)
        
    def post(self, request):
        form = CadastraUsuario(request.POST)
        dados_form = form.data
        
        form_librarian = CadastraBibliotecario(request.POST)
        dados_form_librarian = form_librarian.data

        usuario_auth = User.objects.create_user(dados_form_librarian['user'], dados_form['email'], dados_form_librarian['password_librarian'])

        u = Usuario(name_usr=dados_form['name_usr'],
                    cpf_usr=dados_form['cpf_usr'],
                    email=dados_form['email'],
                    street=dados_form['street'],
                    number=dados_form['num'],
                    phone=dados_form['phone'],
                    postcard=dados_form['postcard'],
                    city=dados_form['city'],
                    state=dados_form['state'],
                    neighborhood=dados_form['neighborhood'],
                    birth=dados_form['birth'],
                    usuario=usuario_auth,
                    )
        u.save()
        
        u.librarian_set.create(user=dados_form_librarian['user'],
                                password_librarian=dados_form_librarian['password_librarian'],
                                )
         
        return render(request, self.template_name)

class CriarLivro(View):
    template_name = 'registerbook.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = CadastraLivro(request.POST)
        dados_form = form.data

        book = Book(name_book=dados_form['name_book'],
                    author_book=dados_form['author_book'],
                    subject_matter=dados_form['subject_matter'],
                    year=dados_form['year'],
                    edition=dados_form['edition'],
                    publishing_company=dados_form['publishing_company'],
                    )
        book.save()
        return render(request, self.template_name)

def logout_view(request):
        logout(request)
        redirect('/login/')

def login_err_view(request):
    if not request.user.is_authenticated():
        return render_to_response('myapp/login_error.html')

def contact(request):
    return render(request, 'contact.html')

def base(request):
    return render(request, 'base.html')