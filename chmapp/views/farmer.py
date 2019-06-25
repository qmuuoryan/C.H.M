from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ..decorators import farmer_required
from ..forms import FarmerSignUpForm
from ..models import Farmer ,User

class FarmerSignUpView(CreateView):
    model = User
    form_class = FarmerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'farmer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('farmer:index')

@method_decorator([login_required, farmer_required], name='dispatch')
def index(response):
    return render (response,'users/farmers/index.html')