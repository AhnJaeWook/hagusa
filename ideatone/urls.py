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
    path('', inidea.views.home, name = "homepage"),
    path('admin/', admin.site.urls),
    path('login/',inidea.views.login, name="login"),
    path('logout/',inidea.views.logout, name="logout"),
    path('signup/', inidea.views.signup, name = "signup"),
    path('inhome/', inidea.views.inhome, name="inhome"),
    path('inhome/new/',inidea.views.new, name="new"),
    path('inhome/create',inidea.views.create, name = "create"),
    path('inhome/<int:blog_id>',inidea.views.detail, name="detail"),
]
