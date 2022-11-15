from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from app.forms import *
# Create your views here.
def root(request):
    return render(request, "root.html")

def login(request):
   
    return render(request, "login.html")

def sign_up(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    return render(request, "sign_up.html", {"form": form})