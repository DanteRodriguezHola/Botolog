from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Post

def index(request):
    posts = Post.objects.order_by('-date')
    return render(request, '_Blog/index.html', {
        'posts': posts
    })

def detail(request, slug):
    post = get_object_or_404(Post, slug = slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()

            return redirect('blog:detail', slug = slug)

    else:
        form = CommentForm()

    return render(request, '_Blog/detail.html', {
        'post': post,
        'form': form
    })