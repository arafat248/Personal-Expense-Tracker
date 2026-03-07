from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializer import RegisterSerializer # নিশ্চিত করুন আপনার ফাইলে এই নামটি আছে

class AuthViewSet(viewsets.ViewSet):
    
    # ১. রেজিস্ট্রেশন লজিক
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ২. লগইন লজিক
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    # ৩. লগআউট লজিক
    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request)
        return Response({"message": "Logged out successfully!"}, status=status.HTTP_200_OK)