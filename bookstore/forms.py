from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields

from bookstore import models


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={'class':'w-75 mt-3  pt-2 pb-2 ', 'placeholder':'Enter a email'}))
    password = forms.CharField(label='Password', required=True, widget=forms.TextInput(attrs={'class':'w-75 mt-3  pt-2 pb-2 ', 'placeholder':'Enter a password'}))


class UserRegisterForm(UserCreationForm):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class':'w-75 mt-3  pt-2 pb-2 ', 'placeholder':'Enter a full name'}))
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={'class':'w-75 mt-3  pt-2 pb-2 ', 'placeholder':'Enter a email'}))
    password = forms.CharField(label='Password', required=True, widget=forms.TextInput(attrs={'class':'w-75 mt-3  pt-2 pb-2 ', 'placeholder':'Enter a password'}))
    avatar = forms.ImageField(required=True)

    class Meta:
        model = models.UserProfile
        fields = ['name', 'email', 'password', 'avatar']
        
