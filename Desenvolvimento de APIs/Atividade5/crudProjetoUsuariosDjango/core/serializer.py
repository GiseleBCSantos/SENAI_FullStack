from rest_framework import serializers
from .models import Projeto
from django.contrib.auth.models import User

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
