from unicodedata import name

from django.urls import re_path as path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.csspostcss, name='getting-started'),  
    path('cssparameters/', views.cssparameters, name="css-parameters"),
    path('css_intro/', views.cssintro, name="css-intro"),
    path('applying-css/', views.applyingcss, name="applying-css")
]