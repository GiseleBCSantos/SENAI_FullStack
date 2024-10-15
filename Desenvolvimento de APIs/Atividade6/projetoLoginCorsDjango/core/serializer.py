from rest_framework import serializers
from .models import Projeto
from django.contrib.auth.models import User

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'


