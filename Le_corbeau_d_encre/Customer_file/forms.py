from django import forms

class NewCustomForm(forms.Form):
    gender = forms.ChoiceField(required=True)
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    birthday = forms.DateField(required=True)
    adress = forms.CharField()
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    password2 = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].label = "Genre"
        self.fields['gender'].help_text = "Veuillez nous renseigner votre 'genre' pour savoir si votre corps est plus proche de celui d'un homme ou d'une femme."
        self.fields['last_name'].label = "Nom de famille"
        self.fields['first_name'].label = "Prénom"
        self.fields['birthday'].label = "Date de naissance"
        self.fields['birthday'].help_text = "Veuillez nous renseigner votre date de naissance pour savoir si vous êtes majeur."
        self.fields['adress'].label = "Adresse postale"
        self.fields['phone_number'].label = "Adresse email"
        self.fields['password2'].label = "Mot de passe"
