from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_insuranceCompany:
            return redirect('insuranceCompany:index')

        else:
            return redirect('farmer:index')
    return render(request, 'users/home.html')
