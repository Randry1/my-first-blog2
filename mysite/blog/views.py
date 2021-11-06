from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
@login_required()
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #Пока удалил дату публикации чтобы создать черновик
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})
@login_required()
def post_edit(request, pk ):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # Пока удалил дату публикации чтобы создать черновик
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required()
def post_draft_list(request):
    '''Контроллер для показа черновиков постов'''
    post_draft = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'post_draft': post_draft})

@login_required()
def post_publish(request, pk):
    '''Обработка нажатия кнопки публикации'''
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=post.pk)

@login_required()
def post_delete(request, pk):
    '''Обработка нажатия кнопки удалить пост'''
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')