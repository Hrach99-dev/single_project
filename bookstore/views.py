from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LoginView
from django.views.generic import View, ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import logout
from bookstore import forms, models
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# Create your views here.





class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'user_update.html'
    form_class = forms.UserUpdateForm
    queryset = models.UserProfile.objects.all()
    success_url = reverse_lazy('profile')

    def get_object(self):
        id_ = self.request.user.pk
        return get_object_or_404(models.UserProfile, id=id_)

class UserDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'delete_account.html'
    model = models.UserProfile
    success_url = reverse_lazy('login')

    def test_func(self):
        user = self.get_object()
        if self.request.user.pk == user.pk:
            return True
        return False


class AddNewsPageView(LoginRequiredMixin, CreateView):
    template_name = 'add_news.html'
    form_class = forms.NewsCreateForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsDetailView(LoginRequiredMixin, DetailView):
    model = models.News
    template_name = 'news_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = self.get_object()
        user = get_object_or_404(models.UserProfile, email=news.author)
        context["user_name"] = user.name
        context["user_lastname"] = user.last_name
        return context


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'update_news.html'
    form_class = forms.NewsCreateForm
    model = models.News
    
   
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'delete_news.html'
    model = models.News
    success_url = reverse_lazy('profile')

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = self.get_object()
        user = get_object_or_404(models.UserProfile, email=news.author)
        context["user_name"] = user.name
        context["user_lastname"] = user.last_name
        return context






class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = models.News
    context_object_name = 'news'
    paginate_by = 9

class AboutPageView(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'


class ProfilePageView(LoginRequiredMixin, ListView):
    template_name = 'profile.html'
    # model = models.News
    context_object_name = 'news'
    paginate_by = 9
    
    def get_queryset(self):
        return models.News.objects.filter(author=self.request.user)

    







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