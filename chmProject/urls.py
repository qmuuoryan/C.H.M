from django.contrib import admin
from django.urls import include, path

from chmapp.views import farmer, farmhealth, insuranceCompany

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chmapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', farmhealth.SignUpView.as_view(), name='signup'),
    path('accounts/signup/farmer/', farmer.FarmerSignUpView.as_view(), name='farmers_signup'),
    path('accounts/signup/insuranceCompany/', insuranceCompany.InsurancecompanySignUpView.as_view(), name='insuranceCompany_signup'),

]
