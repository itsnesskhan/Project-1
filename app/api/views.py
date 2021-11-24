from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserCreateSerializer, UserUpdateSerializer
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class ApiRoots(generics.GenericAPIView):
    def get(self, request):
        return Response(
            {
                'users':reverse('user-list', request = request),
            }
        )

class UserRegisterApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]

class UserUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]