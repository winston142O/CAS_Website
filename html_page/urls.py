from unicodedata import name
from django.urls import re_path as path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.html_page, name='getting-started'),  
    path('html-intro/', views.html_intro, name='html-intro'),         
    path('html-tags/', views.html_tags, name='html-tags'),     
    path('html-tags2/', views.html_tags2, name='html-tags2'),     
    path('html-tags3/', views.html_tags3, name='html-tags3'),               
    path('html-tags4/', views.html_tags4, name='html-tags4'),               
    
]


