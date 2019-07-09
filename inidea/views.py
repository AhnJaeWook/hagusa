from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

from django.contrib.auth.models import User#user만드는 함수들 가져와
from django.contrib import auth

# Create your views here.
def home(request):#blog 함수임
    blogs = Blog.objects.all()
    return render(request, 'homepage.html', {'blogs':blogs})

def inhome(request):
    blogs = Blog.objects.all()
    return render(request, 'inhome.html', {'blogs':blogs})

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])#유저 만들어줘
                auth.login(request, user)#유저 로그인해줘
                return redirect('homepage')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(request, username = request.POST['username'], password = request.POST['password'])#존재하니?
        if user is not None:
            auth.login(request, user)#로그인
            return redirect('homepage')
    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('homepage')
    return render(request, 'homepage.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    
def detail(request, blog_id):
    details=get_object_or_404(Blog,pk=blog_id)
    return render(request, 'detail.html',{'details':details})