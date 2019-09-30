from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse

from django.contrib.auth.decorators import login_required
from .models import Photo, Comment
from .forms import CommentForm
# Create your views here.

class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'
    
class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.author_id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['author','text','image']
    template_name_suffix = '_update'
    success_url = '/'

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
    success_url = '/'

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

class PhotoLike1(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.like1.all():
                    photo.like1.remove(user)
                else:
                    photo.like1.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)

class PhotoLike2(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.like2.all():
                    photo.like2.remove(user)
                else:
                    photo.like2.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)

class PhotoLike3(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.like3.all():
                    photo.like3.remove(user)
                else:
                    photo.like3.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)
            
class PhotoLike4(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.like4.all():
                    photo.like4.remove(user)
                else:
                    photo.like4.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)
            
class PhotoLike5(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.like5.all():
                    photo.like5.remove(user)
                else:
                    photo.like5.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)

def comment_detail(request, photo_id):
    comment_detail = get_object_or_404(Photo, pk=photo_id)
    comments = Comment.objects.filter(photo_id=photo_id)

    context = {
        'comment_detail' : comment_detail,
        'comments' : comments
    }

    return render(request, 'photo_detail.html', context)

def comment_new(request, post_pk):
    post = get_object_or_404(Photo, pk=post_pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo = post
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
            return redirect('photo:detail',comment.photo.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request,'comment_form.html',{'form':form})

    
def comment_delete(request, post_pk,pk):
    comment = get_object_or_404(Comment, pk=pk)
    #작성자만 삭제가능
    if comment.author != request.user:
        return redirect('photo:detail',post_pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('photo:detail',post_pk)

    return render(request,'comment_confirm_delete.html',{'comment':comment,})
