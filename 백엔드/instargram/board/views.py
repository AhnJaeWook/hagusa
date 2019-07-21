from django.shortcuts import render, get_object_or_404, redirect # redirect를 쓰기 위해 소환!
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'detail':detail})

def new(request):
    return render(request,'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.save()
    return redirect('/home/detail/'+str(blog.id))

def delete(request,blog_id):
    get_object_or_404(Blog,pk=blog_id).delete()
    return redirect('/home/')

def edit(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id) 
    return render(request,'edit.html',{'blog':blog})

def update(request, blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.save()

    return redirect('/home/detail/' + str(blog_id))