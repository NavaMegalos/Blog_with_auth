from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Author, Post, Comentario

class AuthorLoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=150)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
class AuthorCreateForm(UserCreationForm):
    email = forms.EmailField(
        label='Correo', 
        required=True, 
        help_text='', 
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce un correo'}),
        error_messages={'required': 'Este campo es obligatorio'}
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Introduce una contraseña segura'}),
        help_text='',
        error_messages={'required': 'Este campo es obligatorio'}
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña'}),
        help_text='',
        error_messages={'required': 'Este campo es obligatorio'}
    )
    
    class Meta:
        model = Author
        fields = ('username', 'first_name', 'email', 'password1', 'password2')
        
        labels = {
            'username': 'Usuario',
            'email': 'Correo',
            'first_name': 'Nombre'
        }
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Introduce tu nombre de usuario'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Introduce tu email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Introduce tu nombre'}),
        }
        
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
        
        error_messages = {
            'username': {
                'required': "Este campo es obligatorio",
                'unique': "Este nombre de usuario ya está en uso",
            },
            'email': {
                'required': "Este campo es obligatorio",
                'unique': "Este email ya está registrado",
            },
            'password1': {
                'required': "Este campo es obligatorio",
                'min_length': "La contraseña debe tener al menos 8 caracteres",
            },
            'password2': {
                'required': "Este campo es obligatorio",
                'password_mismatch': "Las contraseñas no coinciden",
            },
        }
        

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'contenido')
                
        labels = {
            'titulo': 'Titulo',
            'contenido': 'Contenido',
        }
        
        
class ComentarioCreateForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)