from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('projectcomments', views.projectcomments, name='projectcomments'),
    path('', views.projecthome, name='projecthome'),
    path('<str:slug>', views.projectpost, name='projectpost'),
]