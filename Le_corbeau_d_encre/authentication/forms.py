from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Creation of the form to login :
class LoginForm(forms.Form):
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Mot de passe')

# Creation of the form to new inscription :
class NewCustomForm(forms.Form):
    class Meto(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('gender', 'first_name', 'last_name', 'birthday', 'adress', 'email', 'phone')