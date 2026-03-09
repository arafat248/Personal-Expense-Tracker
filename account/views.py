from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializer import RegisterSerializer


class AuthViewSet(viewsets.ViewSet):
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({
                "user": serializer.data,
                "token": token.key
            })
        return Response(serializer.errors)
    
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key
            })
        return Response({"error": "Invalid credentials"}, status=400)
    
    def logout(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out"})