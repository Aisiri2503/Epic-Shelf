from django.shortcuts import render

def landing(request):
    return render(request,'landing.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')


def about(request):
    return render(request,'about.html')       