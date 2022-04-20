from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Creation of the form to login :
class LoginForm(forms.Form):
    last_name = forms.CharField(required=True, label="Nom de famille ")
    first_name = forms.CharField(required=True, label="Prénom ")
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe ")

# Creation of the form to create a new customer :
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['gender', 'last_name', 'first_name', 'date_of_birth', 'email', 'role']