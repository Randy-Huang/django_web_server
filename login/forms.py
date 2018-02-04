from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    pass

class UserLoginForm(AuthenticationForm):
    pass
