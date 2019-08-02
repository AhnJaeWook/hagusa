from django.shortcuts import render, get_object_or_404, redirect # redirect를 쓰기 위해 소환!
from django.utils import timezone
from .models import Blog, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog_id=blog_id)

    context = {
        'detail' : detail,
        'comments' : comments
    }

    return render(request, 'detail.html', context)

def new(request):
    return render(request,'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.save()
    return redirect('/detail/'+str(blog.id))

def delete(request,blog_id):
    get_object_or_404(Blog,pk=blog_id).delete()
    return redirect('/')

def edit(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id) 
    return render(request,'edit.html',{'blog':blog})

def update(request, blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.save()

    return redirect('/detail/' + str(blog_id))

def comment_new(request, post_pk):
    post = get_object_or_404(Blog, pk=post_pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = post
            comment.author = request.user
            comment.save()
            return redirect('/detail/' + str(post_pk))
    else:
        form = CommentForm()
    return render(request,'comment_form.html',{'form':form})

def comment_edit(request, post_pk,pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if comment.author != request.user:
        return redirect('detail',post_pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES,instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('detail',comment.blog.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request,'comment_form.html',{'form':form})

    
def comment_delete(request, post_pk,pk):
    comment = get_object_or_404(Comment, pk=pk)
    #작성자만 삭제가능
    if comment.author != request.user:
        return redirect('detail',post_pk)

    if request.method == 'POST':
        comment.delete()

    return render(request,'comment_confirm_delete.html',{'comment':comment,})
