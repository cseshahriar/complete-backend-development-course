from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    posts = Post.objects.filter(is_active=True)

    # search 
    title = request.GET.get('title')
    if title is not None:
        posts = posts.filter(title__contains=title)

    # paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'list.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        context = {
            'form': form,
             'is_update': False
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
            'form': form,
             'is_update': False
        }
        return render(request, 'create.html', context)


def post_update(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        messages.success(request, 'Post not found 404!')
        return redirect('post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        context = {
            'form': form,
            'is_update': True
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Post update successfully.')
            return redirect('post_list')
        else:
            return render(request, 'create.html', context)
    else:
        form = PostForm(request.POST or None, instance=post)
        context = {
            'form': form,
            'is_update': True,
        }
        return render(request, 'create.html', context)


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        messages.success(request, 'Post not found 404!')
        return redirect('post_list')

    context = {
        'post': post
    }
    return render(request, 'detail.html', context)

def post_delete(request, pk):
    if request.method == 'POST':
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            messages.success(request, 'Post delete successful!')
            return redirect('post_list')
        except Post.DoesNotExist:
            messages.success(request, 'Post not found 404!')
            return redirect('post_list')
    else:
        messages.success(request, 'Invalid Request')
        return redirect('post_list')