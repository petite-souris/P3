from django.shortcuts import render
from Okohorn.forms import ContactUsForm


def home(request):
    css = "Okohorn/css/home.css"
    return render(request, 'Okohorn/home.html', context={"css": css})


def volva(request):
    css = "Okohorn/css/volva.css"
    return render(request, 'Okohorn/volva.html', context={"css": css})


def contact(request):
    # Add a new form :
    form = ContactUsForm()
    # Pass the form to a gabarit :
    return render(request, 'Okohorn/contact.html', {'form': form})