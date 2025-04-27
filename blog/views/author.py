from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ..forms import AuthorLoginForm, AuthorCreateForm, ComentarioCreateForm
from ..models import Author, Post, Comentario
from ..utils.decorators import redirect_authenticated_user

@redirect_authenticated_user
def login_view(request):
    form = AuthorLoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        author = authenticate(request, username=username, password=password)
        if author is None:
            return HttpResponse("Credenciales invalidas")
        else:
            login(request, author)
            return redirect("blog:home")
    return render(request, 'author/login.html', {'form': form})

def logout_view(request):
    logout(request)
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("Has cerrado sesión")
    else:
        return redirect('blog:home')

@redirect_authenticated_user
def register_view(request):
    form = AuthorCreateForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        if not username or not password or not email:
            return HttpResponse("Todos los campos son requeridos")
        
        if Author.objects.filter(username=username).exists():
            return HttpResponse("El nombre de usuario ya existe")
        if Author.objects.filter(email=email).exists():
            return HttpResponse("Email ya registrado")
        
        new_author = AuthorCreateForm(request.POST)
        if new_author.is_valid():
            new_author.save()
            return redirect('blog:register')
        else:
            return redirect('blog:register')
            
            
    return render(request, 'author/register.html', {'form': form})

@login_required
def author_home(request):
    context = {}
    posts = Post.objects.all().order_by('-fecha_creacion')
    forms = {post.id: ComentarioCreateForm for post in posts}
        
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        form = ComentarioCreateForm(request.POST)
        
        if request.user.is_authenticated and form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.author = request.user
            comentario.save()
            
            return redirect('blog:home')
    
    context = {
        'posts': posts,
        'forms': forms,
    }
    
    return render(request, 'author/home.html', context)