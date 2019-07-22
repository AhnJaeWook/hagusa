from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

from django.contrib.auth.models import User#user만드는 함수들 가져와
from django.contrib import auth

# Create your views here.
def read(request):#blog 함수임
    return render(request, "read.html")

def read1(request):
    return render(request, "read1.html")

def main(request):
    return render(request, "main.html")

def love(request):
    return render(request, "maumdaero.html")
    
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

def new(request):
    return render(request, "new.html")

def pr2(request):
    return render(request, "pr2.html")

def pr22(request):
    return render(request, "pr2.html")

def pratice(request):
    return render(request, "pratice.html")
