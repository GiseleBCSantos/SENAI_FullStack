from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from django.http import Http404

# Create your views here.

class ListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_object(self):
        user = self.request.user
        obj = super().get_object()
        if obj == user:
            return obj
        raise Http404