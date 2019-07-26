"""instargram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings#내 세팅을 가져와라
from django.conf.urls.static import static#url들을 가져와라

import frontend.views#블로그안에 있는 views라는 파이썬 파일을 가져옴
import board.views
import accounts.views
from accounts import views
import photo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),
    path('accounts/', include('accounts.urls')),
    path('read/', photo.views.read, name = "read"),
    path('main/', photo.views.main, name="main"),
    path('bulletin/', photo.views.bulletin, name="bulletin"),
    path('bulletin/intro/', photo.views.bulletinIntro, name="bulletinIntro"),
    path('bulletin/menu/', photo.views.bulletinMenu, name="bulletinMenu"),
    path('bulletin/map/', photo.views.bulletinMap, name="bulletinMap"),
    path('bulletin/com/', photo.views.bulletinComment, name="bulletinComment"),
    path('new1/',photo.views.new1, name="new1"),
    path('pr2/',photo.views.pr2, name="pr2"),
    path('pr22/',photo.views.pr2, name="pr22"),
    path('pratice/',photo.views.pratice, name="pratice"),
    path('pagination/',board.views.home,name='home'),
    path('pagination/detail/<int:blog_id>/',board.views.detail, name="detail"),
    path('pagination/new/',board.views.new,name='new'),
    path('pagination/create/',board.views.create, name="create"),
    path('pagination/delete/<int:blog_id>/', board.views.delete, name="delete"),
    path('pagination/edit/<int:blog_id>/',board.views.edit, name="edit"),
    path('pagination/update/<int:blog_id>/',board.views.update,name='update'),
    path('accounts/',include('allauth.urls')),
    path('logout/',photo.views.logout,name='logout'),
    path('123/',frontend.views.read1,name="read1"),
    path('login1/',frontend.views.login1,name="login1"),
]
