from django.shortcuts import render


def home(request):
    return render(request, 'Customer_file/home.html')
