from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import UserAccount
from .serializers import UserAccountSerializer, UserRegistrationSerializer, MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = [IsAuthenticated]

class UserRegistrationView(generics.CreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserRegistrationSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
