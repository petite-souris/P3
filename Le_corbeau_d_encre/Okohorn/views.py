from django.shortcuts import render


def home(request):
    return render(request, 'Okohorn/home.html')


def volva(request):
    return render(request, 'Okohorn/volva.html')
