from django.contrib.auth.decorators import login_required
from authentication import models
from django.shortcuts import render
from . import models

def home(request):
    css = "Customer_file/css/home.css"
    return render(request, 'Customer_file/home.html', {"css":css})


def new_customer(request):
    return render(request, 'Customer_file/inscription.html')

# @login_required
def user_page(request):
    css = "Customer_file/css/user_page.css"
    return render(request, 'Customer_file/user_page.html', {"css":css})