from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.decorators import auth_user
from app.forms import *
from app.models import *
# Create your views here.
@login_required(login_url='login')
def root(request):
    
    return render(request, "root.html", {"all": viewing_all()})

@login_required(login_url='login')
def create(request):
    form = CreateCharForm()
    if request.method == 'POST':
        form = CreateCharForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            origin = form.cleaned_data["origin"]
            powers = form.cleaned_data["powers"]
            occupation = form.cleaned_data["occupation"]
            ethnicity = form.cleaned_data["ethnicity"]
            content = {"form": form, "char": creating(name, origin, powers, occupation, ethnicity)}
            return redirect('root')
        return render(request, "create.html", content)
    else:
        return render(request, "create.html", {'form':form})

@login_required(login_url='login')
def randomize(request):
    random_char = random_character()
    form = CreateCharForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('root')
    return render(request, 'randomize.html', {"random_char": random_char, "form": form})
     
  
@login_required(login_url='login')
def update(request, char_id):
    character = Character.objects.get(pk=char_id)
    form = CreateCharForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('root')
    return render(request, 'update.html', {"character": character, "form": form})

@login_required(login_url='login')
def delete(request, char_id):
    character = Character.objects.get(pk=char_id)
    character.delete()
    return redirect('root')

@auth_user
def sign_up(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('login')
        else: 
            print(form.errors)
    return render(request, "sign_up.html", {"form": form})

@auth_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('root')
        else:
            messages.info(request, 'Username or Password is incorrect :(')

    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect('login')