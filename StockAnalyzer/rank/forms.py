from django import forms
#from django.contrib.auth.models import User
#from resume.models import School, Company, ResumeRepository, Summary, Education, Experience, Skills, Accomplishment, References, Languages
#from .models import Profile
#from django.contrib.auth.forms import UserCreationForm

class IndexSignUpForm(forms.Form):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=False)
    password1 = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)
