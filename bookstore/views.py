from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import View ,ListView, TemplateView, FormView, CreateView
from django.contrib import messages
from bookstore import forms
from django.urls import reverse_lazy

from bookstore import models
from django.contrib.auth.hashers import make_password
# Create your views here.


class HomePageView(TemplateView):
    
    template_name = 'index.html'
    
    

class RegistrationPageView(CreateView):
    form_class = forms.UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    success_message = "Your profile was created successfully"

    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        

    
    
        
class LoginPageView(FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm
    

    