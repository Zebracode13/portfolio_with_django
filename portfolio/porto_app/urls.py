from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from porto_app import views

app_name = 'porto_app'

urlpatterns = [
    path('zs', views.home, name="home"),
]