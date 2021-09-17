from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Comentario, Post,Category
from django.forms import fields, widgets

choice_list = []
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class PostForm(forms.ModelForm):
    choices = Category.objects.all().values_list('name','name')
    for item in choices:
        choice_list.append(item)
    class Meta:
        model=Post 
        fields= ('title','user','content','category')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={ 'class':'form-control','style':'resize: none;'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comentario 
        fields= ('comentario',)
        widgets={
            'comentario':forms.Textarea(attrs={ 'class':'form-control','style':'resize: none;'})
        }