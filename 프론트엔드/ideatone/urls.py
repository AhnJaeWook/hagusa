"""ideatone URL Configuration

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
from django.urls import path

import inidea.views#블로그안에 있는 views라는 파이썬 파일을 가져옴

from django.conf import settings#내 세팅을 가져와라
from django.conf.urls.static import static#url들을 가져와라

urlpatterns = [
    path('love/',inidea.views.love, name="love"),
    path('read/', inidea.views.read, name = "read"),
    path('read1/', inidea.views.read1, name= "read1"),
    path('admin/', admin.site.urls),
    path('', inidea.views.main, name="main"),
    path('admin/', admin.site.urls),
    path('bulletin/', inidea.views.bulletin, name="bulletin"),
    path('bulletin/intro/', inidea.views.bulletinIntro, name="bulletinIntro"),
    path('bulletin/menu/', inidea.views.bulletinMenu, name="bulletinMenu"),
    path('bulletin/map/', inidea.views.bulletinMap, name="bulletinMap"),
    path('bulletin/com/', inidea.views.bulletinComment, name="bulletinComment"),
]
