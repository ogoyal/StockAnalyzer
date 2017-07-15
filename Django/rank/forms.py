from django import forms

class IndexSignUpForm(forms.Form):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=False)
    password1 = forms.CharField(widget = forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget = forms.PasswordInput, label="Confirm Password")
