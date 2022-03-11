from django.db import models


class Modulo(models.Model):
    objects = None
    titulo = models.CharField(max_length=64)
