# apps/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class AmsUser(AbstractUser):  # or Account - whatever you named it
    AccountID = models.AutoField(primary_key=True)
    #EmployeeID = models.CharField(max_length=100, blank=True)
    # FirstName - REMOVE (already in AbstractUser as first_name)
    # LastName - REMOVE (already in AbstractUser as last_name)
    # Password - REMOVE (already in AbstractUser)
    Permissions = models.CharField(max_length=100, default='viewer')
    Status = models.CharField(max_length=50, default='active')
    
    # Fix the groups and permissions clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='ams_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='ams_users',
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Use lowercase (Django's built-in)