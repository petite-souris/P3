from django.shortcuts import render
from Okohorn.forms import ContactUsForm


def home(request):
    return render(request, 'Okohorn/home.html')


def volva(request):
    return render(request, 'Okohorn/volva.html')


def contact(request):
    # Add a new form :
    form = ContactUsForm()
    # Pass the form to a gabarit :
    return render(request, 'Okohorn/contact.html', {'form': form})
