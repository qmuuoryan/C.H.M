from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import insuranceCompany_required
from ..forms import InsurancecompanySignupForm
from ..models import User

class InsurancecompanySignUpView(CreateView):
    model = User
    form_class = InsurancecompanySignupForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'insuranceCompany'
        return super().get_context_data(**kwargs)

    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('insuranceCompany:index')

@method_decorator([login_required, insuranceCompany_required], name='dispatch')
def index(response):
    return render(response, 'users/insuranceCompany/index.html')