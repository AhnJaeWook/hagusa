from django.shortcuts import render, get_object_or_404, redirect # redirect를 쓰기 위해 소환!
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.


def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    total_len = len(blog_list)

    paginator = Paginator(blog_list, 1)
    page = request.GET.get('page')

    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    

    index = posts.number -1
    max_index = len(paginator.page_range)
    start_index = index - 2 if index>=2 else 0

    if index < 2:
        end_index = 5-start_index
    else:
        end_index = index+3 if index <= max_index -3 else max_index
    
    
    page_range = list(paginator.page_range[start_index:end_index])

    return render(request, 'home.html',{'blogs':blogs,'posts':posts,'blog_list':blog_list,'page_range':page_range,'total_len':total_len,'max_index':max_index-2})

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
    return redirect('/pagination/detail/'+str(blog.id))

def delete(request,blog_id):
    get_object_or_404(Blog,pk=blog_id).delete()
    return redirect('/pagination/')

def edit(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id) 
    return render(request,'edit.html',{'blog':blog})

def update(request, blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.save()

    return redirect('/pagination/detail/' + str(blog_id))