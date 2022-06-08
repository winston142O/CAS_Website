from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'home_page/index.html')

def about(request):
    return render(request, 'home_page/about.html', {'title': 'About'})

def classes(request):
    return render(request, 'home_page/classes.html',{'title': 'Classes'})