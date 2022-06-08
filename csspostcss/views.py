from django.shortcuts import render

# Create your views here.

def csspostcss(request):
    return render(request, 'csspostcss/csspostcss.html')

def cssparameters(request):
    return render(request, 'csspostcss/cssparameters.html')

def cssintro(request):
    return render(request, 'csspostcss/cssintro.html')

def applyingcss(request):
    return render(request, 'csspostcss/applying_css.html')