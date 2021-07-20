from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from PIL import Image


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, name, email, password=None, avatar=None):
        """Create a new user profile"""

        if not email:
            raise ValueError('User must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.avatar = avatar
        user.save(using=self._db)

        return user
    
    def create_superuser(self, name, email, password, avatar=None):
        """Create ans save a new superuser with given details"""
        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.avatar = avatar
        user.save(using=self._db)

        return user
    
        

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    
   
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='static/images/users/'+ datetime.datetime.now().strftime('%Y-%m-%d'))

    objects = UserProfileManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name


    def __str__(self) -> str:
        """Return email of user"""
        return self.email