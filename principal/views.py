from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import UserRegisterForm
# Create your views here.

def feed(request):
  return render(request, 'principal/feed.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = { 'form' : form}
    return render(request, 'principal/register.html',context)

def profile(request):
    return render(request, 'principal/profile.html')

def crear(request):
    return render(request, 'principal/crear.html')

def editar(request):
    return render(request, 'principal/editar.html')



