from django.shortcuts import render

# Create your views here.

def html_page(request):
    return render(request, 'html_page/html_themes.html')

def html_intro(request):
    return render(request, 'html_page/html_intro.html', {'title': 'html-intro'})

def html_tags(request):
    return render(request, 'html_page/html_tags.html', {'title': 'html-tags'})

def html_tags2(request):
    return render(request, 'html_page/html_tags2.html', {'title': 'html-tags2'})

def html_tags3(request):
    return render(request, 'html_page/html_tags3.html', {'title': 'html-tags3'})

def html_tags4(request):
    return render(request, 'html_page/html_tags4.html', {'title': 'html-tags4'})