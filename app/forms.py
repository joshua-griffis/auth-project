from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from app.models import *
from django.forms import ModelForm
    


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CreateCharForm(ModelForm):
    class Meta:
        model = Character
        fields = "__all__"

