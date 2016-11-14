from __future__ import unicode_literals

from django.db import models



class Registrado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    codigo_postal = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    profile = models.ImageField(upload_to='/profiles')

    def __unicode__(self): # en python 3 es __str__
        return self.email