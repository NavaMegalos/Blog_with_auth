from django.shortcuts import redirect, render
from ..models import Post
from ..forms import PostCreateForm
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    form = PostCreateForm()
    
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:home')
    
    return render(request, 'post/create_post.html', {'form': form})    
    