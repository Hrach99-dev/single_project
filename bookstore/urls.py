
from django.urls import path

from bookstore import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('profile', views.ProfilePageView.as_view(), name='profile'),
    path('profile/update', views.UserUpdateView.as_view(), name='user_update'),
    path('profile/<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete_account'),
    path('register', views.RegistrationPageView.as_view(), name='register'),
    path('login', views.LoginPageView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('news/add', views.AddNewsPageView.as_view(), name='add_news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),
] 
