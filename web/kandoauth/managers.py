"""
Custom model managers for Kando auth module.
"""
from django.contrib.auth.models import BaseUserManager


class KandoUserManager(BaseUserManager):
    """
    User manager class that implements create_user and create_superuser
    methods for creating normal and admin users respectively.
    """

    def create_user(self, email, first_name, last_name, profile_pic=None, password=None):
        """
        Creates and saves a User with the given email, first name,
        last name, profile pic if given, and a password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            profile_pic=profile_pic,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, profile_pic=None, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            profile_pic=profile_pic,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
