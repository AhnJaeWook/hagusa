from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

from django.contrib.auth.models import User#user만드는 함수들 가져와
from django.contrib import auth

# Create your views here.
def main(request):
    return render(request, 'main.html')

def homepage(request):#blog 함수임
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

def frontnew(request):
    return render(request, 'frontnew.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    
def frontdetail(request, blog_id):
    details=get_object_or_404(Blog,pk=blog_id)
    return render(request, 'frontdetail.html',{'details':details})

def delete(request, blog_id):
    get_object_or_404(Blog, pk=blog_id).delete()

    return redirect('/')

def edit(request, blog_id):
    blog= get_object_or_404(Blog,pk=blog_id)
    return render(request, 'edit.html', {'blog':blog})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.save()

    return redirect('/detail/' + str(blog_id))

def infronthome(request):
    return render(request, "infronthome.html")

def fronthome(request):
    return render(request, "fronthome.html")

def bulletin(request):
    return render(request, "bulletin.html")

def bulletinMenu(request):
    return render(request, "bulletin_menu.html")

def bulletinIntro(request):
    return render(request, "bulletin_introduce.html")

def bulletinMap(request):
    return render(request, "bulletin_map.html")

def bulletinComment(request):
    return render(request, "bulletin_comment.html")