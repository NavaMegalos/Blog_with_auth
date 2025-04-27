from django.urls import path
from .views.author import login_view, logout_view, register_view, author_home
from .views.post import create_post

app_name = 'blog'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('home/', author_home, name='home'),
    path('post/create', create_post, name='create_post')
]