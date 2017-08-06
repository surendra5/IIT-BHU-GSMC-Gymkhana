from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    url(r'^eventform/$', views.GymkhanaFormCreate, name='GymkhanaFormCreate'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page_name>\w+)/', views.gamer, name='gamer'),


]