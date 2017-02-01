"""
Custom auth models for Kando.
"""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from kandoauth.managers import KandoUserManager

from tools.models import KandoModelBase


class KandoUser(AbstractBaseUser, KandoModelBase, PermissionsMixin):
    """
    Custom user model to allow email to map to username field.
    """
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField(
        default=True,
        help_text='Designates whether this user should be treated'
        'as active. Unselect this instead of deleting accounts.')

    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.TextField()
    last_name = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pic', null=True, blank=True)
    objects = KandoUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        # The user is identified by their first name plus last name
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        # The user is identified by their first name
        return self.first_name

    def __str__(self):
        return self.email
