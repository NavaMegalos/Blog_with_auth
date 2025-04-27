from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    # password = models.CharField(max_length=100)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='author_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='author_permissions',
        blank=True,
    )

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    