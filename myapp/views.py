from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def content(request):
    return render(request, "content.html")

def page(request):
    return render(request, "404.html")