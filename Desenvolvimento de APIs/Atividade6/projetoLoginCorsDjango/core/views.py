from django.shortcuts import render
from .models import Projeto
from django.contrib.auth.models import User
from .serializer import ProjetoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class ListCreateProjetoView(ListCreateAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class RetrieveUpdateDestroyProjetoView(RetrieveUpdateDestroyAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer



