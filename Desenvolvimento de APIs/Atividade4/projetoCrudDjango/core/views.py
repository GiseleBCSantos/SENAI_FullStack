from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Projeto
from .serializer import ProjetoSerializer



# Create your views here.

class ListCreateProjetoAPIView(ListCreateAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class RetrieveUpdateDestroyProjetoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer