from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class Usuario(models.Model):
    name_usr = models.CharField(max_length=100, default='', null=False)
    cpf_usr = models.CharField(max_length=11, default='', null=False)
    email = models.CharField(max_length=50, default='', null=False)
    street = models.CharField(max_length=255, default='', null=False)
    number = models.IntegerField(null=False)
    phone = models.CharField(max_length=14, default='', null=False)
    postcard = models.CharField(max_length=10, default='', null=False)
    city = models.CharField(max_length=50, default='', null=False)
    state = models.CharField(max_length=20, default='', null=False)
    neighborhood = models.CharField(max_length=50, default='', null=False)
    birth = models.CharField(max_length=20, default='', null=False)
    usuario = models.OneToOneField(User,related_name="polls")

class Student(models.Model):
    registration = models.IntegerField(null=False)
    password_student = models.CharField(max_length=8, default='', null=False)
    user_student = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Librarian(models.Model):
    user = models.CharField(max_length=14, default='', null=False)
    password_librarian = models.CharField(max_length=8, default='', null=False)
    user_librarian = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Book(models.Model):
    name_book = models.CharField(max_length=100, default='', null=False)
    author_book = models.CharField(max_length=100, default='', null=False)
    subject_matter = models.CharField(max_length=100, default='', null=False)
    year = models.IntegerField(null=False)
    edition = models.CharField(max_length=10, default='', null=False)
    publishing_company = models.CharField(max_length=100, default='', null=False)

class Loan(models.Model):
    date_loan = models.CharField(max_length=10, default='', null=False)
    data_devolution = models.CharField(max_length=10, default='', null=False)
    user_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    book_rented = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    user_librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE, null=False)

class Devolution(models.Model):
    date_devolution = models.CharField(max_length=10, default='', null=False)
    user_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    book_loan = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)

class Renovation(models.Model):
    date_renovation = models.CharField(max_length=10, default='', null=False)
    date_shelf_life = models.CharField(max_length=10, default='', null=False)
    user_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    book_renovation = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)

class Reserve(models.Model):
    data_reserve = models.CharField(max_length=10, default='', null=False)
    data_shelf_life = models.CharField(max_length=10, default='', null=False)
    user_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    book_reserve = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)