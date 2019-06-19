from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from users.models import (Farmer,User)

class InsurancecompanySignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self,commit = True):
        user = super().save(commit=False)
        user.is_insuranceCompany = True
        if commit:
            user.save()
        return user


class FarmerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_farmer = True
        user.save()
        return user
