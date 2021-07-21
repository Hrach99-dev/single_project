from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from bookstore import models


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Email',
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class':'w-75 mt-3 pt-2 pb-2', 
                'placeholder':'Enter a email',
                'autofocus': False
            }
        )
    )
    password = forms.CharField(
        label='Password', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'class':'w-75 mt-3 pt-2 pb-2', 
                'placeholder':'Enter a password'
            }
        )
    )

class UserRegisterForm(UserCreationForm):
    name = forms.CharField(
        label='First name', 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class':'w-75 mt-3 pt-2 pb-2', 
                'placeholder':'Enter a first name',
                'autofocus': 'off'
            }
        )
    )
    last_name = forms.CharField(
        label='Last name', 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class':'w-75 mt-3 pt-2 pb-2', 
                'placeholder':'Enter a last name',
            }
        )
    )
    email = forms.CharField(
        label='Email', 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class':'w-75 mt-3 pt-2 pb-2', 
                'placeholder':'Enter a email',
                'autocomplete':'off'
            }
        )
    )
    password1 = forms.CharField(
        label='Password', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'class':'w-75 mt-3 pt-2 pb-2', 
                'placeholder':'Enter a password',
            }
        ),
    )

    password2 = forms.CharField(
        label='Confirm password', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'class':'w-75 mt-3 pt-2 pb-2', 
                'placeholder':'Confirm password',
            }
        )
    )

  

    class Meta:
        model = models.UserProfile
        fields = ['name', 'last_name', 'email']
