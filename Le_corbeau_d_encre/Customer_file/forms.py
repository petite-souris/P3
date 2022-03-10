from django import forms


class LoginForm(forms.Form):
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    password = forms.PasswordInput()


class NewCustomForm(forms.Form):
    gender = forms.ChoiceField(required=True)
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    birthday = forms.DateField(required=True)
    adress = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.IntegerField(required=True)
    password = forms.PasswordInput()
