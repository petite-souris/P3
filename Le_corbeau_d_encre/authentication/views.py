from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.conf import settings 
from . import forms

def logout_user(request):
    # Use the function logout to go out :
    logout(request)
    # Return in using redirect function to redirect at login page :
    return redirect('login')

def login_page(request):
    # Display form creted with abstractuser :
    form = forms.LoginForm()
    # Verify if the form is complete. If it's complete, make the method :
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        # Verify if field are validate and send a message if it's not validate :
        if form.is_valid():
            user = authenticate(first_name=form.cleaned_data['first_name'], 
                last_name=form.cleaned_data['last_name'], password1=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                message = f'Bienvenue {user.first_name} {user.last_name}, vous êtes connecté(e) {{/user_home}}'
                return redirect ('user_page')
            else:
                message = 'Identifiants invalides, veuillez recommencer s il-vous-plaît.'
                return redirect ('home_custom')

    css = "authentication/css/login_style.css"
    return render(request, 'authentication/login.html', context = {'form': form , "css":css})

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        #condition si le formulaire est valide, on sauve le formulaire et on le login
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('user_page')

    css = "authentication/css/inscription_style.css"
    return render(request, 'authentication/inscription.html', context={'form': form, "css":css})