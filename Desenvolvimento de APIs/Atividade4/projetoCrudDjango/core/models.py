from django.db import models

# Create your models here.

class Projeto(models.Model):
    nomeDoProjeto = models.CharField(max_length=100, null=False, blank=False)
    area = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(null=False, blank=False)
