from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def post_list(request):
    posts = Post.objects.filter(is_active=True)

    context = {
        'posts': posts,
    }
    return render(request, 'list.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully.')
            return redirect('post_list')
        else:
            return render(request, 'create.html', context)
    else:
        form = PostForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'create.html', context)