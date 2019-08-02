"""prace_instargram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import thisisapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',thisisapp.views.home,name='home'),
    path('detail/<int:blog_id>/',thisisapp.views.detail, name="detail"),
    path('new/',thisisapp.views.new,name='new'),
    path('create/',thisisapp.views.create, name="create"),
    path('delete/<int:blog_id>/', thisisapp.views.delete, name="delete"),
    path('edit/<int:blog_id>/',thisisapp.views.edit, name="edit"),
    path('update/<int:blog_id>/',thisisapp.views.update,name='update'),
    path(r'^(?P<post_pk>\d+)/comment/new/$',thisisapp.views.comment_new,name='comment_new'), 
    path(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)/edit/$',thisisapp.views.comment_edit,name='comment_edit'), 
    path(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)/delete/$',thisisapp.views.comment_delete,name='comment_delete'), 
]
