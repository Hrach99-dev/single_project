from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from PIL import Image
from django.urls import reverse






class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""

        if not email:
            raise ValueError('User must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create ans save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.last_name = ''
        user.profile_image = None
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    
   
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    biography = models.TextField(default='')
    email = models.EmailField(max_length=255, unique=True)
    quote = models.TextField(default='')
    date_joined = models.DateTimeField(verbose_name="date joines", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='static/images/users/' + datetime.datetime.now().strftime('%Y-%m-%d'), default='default_user.png')

    objects = UserProfileManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name


    def __str__(self) -> str:
        """Return email of user"""
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=40)

class Book(models.Model):
   name = models.CharField(max_length=300)
   pages = models.IntegerField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
   authors = models.ManyToManyField(UserProfile)
   categories = models.ManyToManyField(Category)
   pubdate = models.DateField()
   image = models.ImageField(upload_to='static/images/books/' + datetime.datetime.now().strftime('%Y-%m-%d'))

class Store(models.Model):
   name = models.CharField(max_length=300)
   books = models.ManyToManyField(Book)

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='static/images/news/' + datetime.datetime.now().strftime('%Y-%m-%d'))


    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})