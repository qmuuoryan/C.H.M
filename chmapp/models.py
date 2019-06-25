# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

# Create your models here.
#farmer models

class User(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_insuranceCompany = models.BooleanField(default=False)

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    