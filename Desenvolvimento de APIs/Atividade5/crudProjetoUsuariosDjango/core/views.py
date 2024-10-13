from django.shortcuts import render
from .models import Projeto
from django.contrib.auth.models import User
from .serializer import ProjetoSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class ListCreateProjetoView(ListCreateAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class RetrieveUpdateDestroyProjetoView(RetrieveUpdateDestroyAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class ListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
