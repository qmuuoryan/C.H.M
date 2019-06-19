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
    user = models.OneToOneField(User , on_delete=models.CASCADE, primary_key=True)
    """chm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from users.views import farmer, farmhealth, insuranceCompany

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('frontend.urls')),
    path('',include('leads.urls')),
    path('auth/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', farmhealth.SignUpView.as_view(), name='signup'),
    path('accounts/signup/farmer/', farmer.FarmerSignUpView.as_view(), name='farmers_signup'),
    path('accounts/signup/insuranceCompany/', insuranceCompany.InsurancecompanySignUpView.as_view(), name='insuranceCompany_signup'),

]
