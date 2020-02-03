# Django
from django.db import models


class User(models.Model):

    email = models.EmailField()
    password = models.CharField(max_length=100)

    fist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
