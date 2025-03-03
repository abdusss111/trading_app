from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer
User = get_user_model()

# 🔹 List all users & Create new user
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only Admins can list/create users

# 🔹 Retrieve, Update & Delete user by ID
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access
