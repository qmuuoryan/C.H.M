from chmapp.models import User, Farmer
from rest_framework import viewsets,permissions
from .serializers import FarmerSerializer, UserSerializer

#lead viewset...renders/creates a full crud api easily
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FarmerSerializer





