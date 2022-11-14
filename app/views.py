from django.shortcuts import render
from app.forms import *

def root(request):
    return render(request, 'root.html')
