from django.shortcuts import render
from Customer_file.forms import LoginForm, NewCustomForm


def home(request):
    return render(request, 'Customer_file/home.html')


def login(request):
    # Add a new form :
    form = LoginForm()
    # Pass the form to a gabarit :
    return render(request, 'Customer_file/login.html', {'form': form})


def new_custom(request):
    # Add a new form :
    form = NewCustomForm()
    # Pass the form to a gabarit :
    return render(request, 'Customer_file/new_custom.html', {'form': form})

def user_page(request):
    return render(request, 'Customer_file/user_page.html')
