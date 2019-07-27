from django.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.contrib.auth import views as auth_views
import accounts.views

import board.views
app_name = "accounts"

urlpatterns = [
    path('main/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
]