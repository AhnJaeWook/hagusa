from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from django.views.generic.base import View
from django.utils import timezone
from django.contrib.auth.models import User#user만드는 함수들 가져와
from django.contrib import auth
from urllib.parse import urlparse

from .models import Photo, Blog
# Create your views here.

class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_lost'

class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = "/"

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['author', 'text', 'image']
    template_name_suffix = '_update'
    #success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없습니다.')
            return HttpResponseRedirect('/')
            # 삭제 페이지에서 권한이 없다! 라고 띄우거나
            # detail페이지로 들어가서 삭제에 실패했습니다. 라고 띄우거나
        else:
            return super(PhotoUpdate, self).dispatch(request, *args, **kwargs)

class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PhotoDelete, self).dispatch(request, *args, **kwargs)

class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'
    
class PhotoLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.like.all():
                    photo.like.remove(user)
                else:
                    photo.like.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)

class Photofavorite(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.favorite.all():
                    photo.favorite.remove(user)
                else :
                    photo.favorite.add(user)
            return HttpResponseRedirect('/')

def read(request):#blog 함수임
    return render(request, "read.html")

def main(request):
    return render(request, "main.html")
    
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

def new1(request):
    return render(request, "new1.html")

def pr2(request):
    return render(request, "pr2.html")

def pratice(request):
    return render(request, "pratice.html")

def logout(request):
    auth.logout(request)
    return redirect('/main')