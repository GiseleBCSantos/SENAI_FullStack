from django.db import models

# Create your models here.

class Projeto(models.Model):
    nomeDoProjeto = models.CharField(max_length=100, blank=False, null=False)
    area = models.CharField(max_length=100, blank=False, null=False)
    status = models.BooleanField(blank=False, null=False)


