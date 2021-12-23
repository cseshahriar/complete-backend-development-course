from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm

# for class base views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

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
    
    
    
# class base views
class PostListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'cbv_list.html'
    
 
    def get_queryset(self, *args, **kwargs):
        queryset = Post.objects.filter(is_active=True)
        
        # search 
        title = self.request.GET.get('title')
        if title is not None:
            queryset = queryset.filter(title__contains=title)
        
        return queryset
    

class PostDetailView(DetailView):
    """ Post detail view """
    model = Post
    template_name = 'cbv_detail.html'
    
    
class PostCreateView(CreateView):
    """ Post create view """
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    success_url = reverse_lazy('cbv_post_list')
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user  # current user
        self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        messages.success(self.request, 'Post has been created successfully')
        return self.success_url
    

class PostUpdateView(UpdateView):
    """ Post update view """
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    success_url = reverse_lazy('cbv_post_list')
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user  # current user
        self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        messages.success(self.request, 'Post has been update successfully')
        return self.success_url
    
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('cbv_post_list')
    
    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        messages.success(self.request, 'Post has been deleed successfully')
        return self.success_url
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.pop('pk', None)
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
        except Post.DoesNotExist:
            messages.success(request, 'Post not found 404!')
            return redirect('cbv_post_list')
        
        return self.delete(request, *args, **kwargs)