# from django.urls import include, path
# from .views import farmhealth, farmer, insuranceCompany
from rest_framework import routers
from .api import UserViewSet, FarmerViewSet
# urlpatterns = [
#     path('', farmhealth.home, name='home'),
#     path('farmer/', include(([ path('', farmer.index, name='index'),], 'farmhealth'), namespace='farmer')),
#     path('insuranceCompany/', include(([ path('', insuranceCompany.index, name='index'), ], 'farmhealth'), namespace='insuranceCompany')),

# ]
router = routers.DefaultRouter()
router.register('api/chmapp/User', UserViewSet, 'user')
router.register('api/chmapp/Farmer', FarmerViewSet, 'farmer')

urlpatterns = router.urls