from django.urls import include, path

from .views import farmhealth, farmer, insuranceCompany

urlpatterns = [
    path('', farmhealth.home, name='home'),

    path('farmer/', include(([ path('', farmer.index, name='index'),], 'farmhealth'), namespace='farmer')),
    path('insuranceCompany/', include(([ path('', insuranceCompany.index, name='index'), ], 'farmhealth'), namespace='insuranceCompany')),

]