from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    posts = Post.objects.order_by('-date')
    return render(request, '_Blog/index.html', {
        'posts': posts
    })

def detail(request, slug):
    post = get_object_or_404(Post, slug = slug)

    return render(request, '_Blog/detail.html', {
        'post': post
    })