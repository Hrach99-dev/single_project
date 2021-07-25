from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import TextInput
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

    error_messages = {
        'invalid_login': (
            "Please enter a correct email and password."
        ),
    }

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
    email = forms.EmailField(
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

class UserUpdateForm(forms.ModelForm):
    

    class Meta:
        model = models.UserProfile
        fields = ['name', 'last_name', 'biography', 'quote', 'profile_image']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'w-100 mt-3 pt-2 pb-2',
                    'placeholder':'Enter a name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'w-100 mt-3 pt-2 pb-2',
                    'placeholder':'Enter a surname',
                }
            ),
            'biography': forms.Textarea(
                attrs={
                    'rows':5,
                    'class': 'mt-3 w-100 user_update_textarea',
                    'placeholder':'Enter a biography',
                    
                }
            ),
            'quote': forms.Textarea(
                attrs={
                    'rows':5,
                    'class': 'mt-3 w-100 user_update_textarea',
                    'placeholder':'Enter a quote',
                    
                }
            ),
            'profile_image': forms.FileInput()
        }


class NewsCreateForm(forms.ModelForm):
    
    class Meta:
        model = models.News
        fields = ['title', 'text', 'image']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'w-100 mt-3 pt-2 pb-2',
                    'placeholder':'Enter a title',
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'rows':5,
                    'class': 'mt-3 w-100 user_update_textarea',
                    'placeholder':'Enter a text',
                    
                }
            ),
            
            'image': forms.FileInput()
        }
    