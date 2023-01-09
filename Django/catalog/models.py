from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Ingresa el nombre del genero")

"""
#Esto nos va a devolver la variable name en formato string.
    def __str__(self):
        return self.name

#Se le agrega una foreign key, es una referencia. Creando una relacion.

class Book(models.Model):
    title = models.CharField(max_length=32)
    summary = models.TextField(max_length=100, help_text="De que trata el libro?: ")
    isbn = models.CharField('ISBN', max_length=13, help_text="El ISBN es de 13 caracteres.")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

"""