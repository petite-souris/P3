from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    # forms.PasswordInput permit to character to stay hidden:
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
