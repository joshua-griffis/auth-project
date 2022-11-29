from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CreateCharForm(forms.Form):
    name = forms.CharField()
    origin = forms.CharField()
    powers = forms.CharField()
    occupation = forms.CharField()
    ethnicity = forms.CharField()