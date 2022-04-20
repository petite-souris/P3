from django.contrib.auth.decorators import login_required
from authentication import models
from django.shortcuts import render
from . import models

def home(request):
    css = "Customer_file/css/home.css"
    return render(request, 'Customer_file/home.html', {"css":css})

# @login_required
def user_page(request):
    css = "Customer_file/css/user_page.css"
    return render(request, 'Customer_file/user_page.html', {"css":css})

# @login_required
def choices(request):
    css = "Customer_file/css/choices.css"
    return render(request, 'Customer_file/choices.html', {"css":css})

def new_project(request):
    css = "Customer_file/css/new_project.css"
    return render(request, 'Customer_file/new_project.html', {"css":css})

def height(request):
    css = "Customer_file/css/height.css"
    return render(request, 'Customer_file/height.html', {"css":css})

def style(request):
    css = "Customer_file/css/style.css"
    return render(request, 'Customer_file/style.html', {"css":css})