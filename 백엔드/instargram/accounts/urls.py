from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin

import board.views
app_name = "accounts"

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
]