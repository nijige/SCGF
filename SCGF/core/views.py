from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'pages/login.html')

def home(request):
    return render(request, 'pages/home.html')

def group(request):
    return render(request, 'pages/group.html')