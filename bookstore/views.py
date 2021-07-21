from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import logout
from bookstore import forms
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# Create your views here.




class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


    
class RegistrationPageView(CreateView):
    form_class = forms.UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    success_message = "Your profile was created successfully"



class LoginPageView(LoginView):
    template_name = 'login.html'
    form_class = forms.LoginForm


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)  