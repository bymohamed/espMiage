from django.db import models

# Create your models here.
class Temperature(models.Model):
    who = models.CharField(max_length=20)
    valeur = models.FloatField(blank=True)
    datetime = models.DateTimeField(auto_now=True)
