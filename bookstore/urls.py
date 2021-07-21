
from django.urls import path

from bookstore import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('register', views.RegistrationPageView.as_view(), name='register'),
    path('login', views.LoginPageView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
] 
