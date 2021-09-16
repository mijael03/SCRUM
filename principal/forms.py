from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Comentario, Post
from django.forms import fields, widgets

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class PostForm(forms.ModelForm):
    class Meta:
        model=Post 
        fields= ('title','user','content')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={ 'class':'form-control','style':'resize: none;'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comentario 
        fields= ('comentario',)
        widgets={
            'comentario':forms.Textarea(attrs={ 'class':'form-control','style':'resize: none;'})
        }