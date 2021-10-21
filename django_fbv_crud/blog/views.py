from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(is_active=True)

    context = {
        'posts': posts,
    }
    return render(request, 'list.html', context)