from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm

# Create your models here.
class Esp(models.Model):
    mac = models.CharField(max_length=20, primary_key=True)
    def __str__(self):
        return 'Esp, mac : {}'.format(self.mac)

class ClasseNum(models.Model):
    num = models.IntegerField(primary_key=True)
    etage = models.IntegerField(blank=True)
    def __str__(self):
        return 'Salle s{} etage {}'.format(self.num, self.etage)

class Temperature(models.Model):
    who = models.ForeignKey(Esp, on_delete=models.CASCADE)
    valeur = models.FloatField(blank=True)
    datetime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'temperature {} mesured by {} in {}'.format(self.valeur, self.who, self.datetime)

class SalleDeClasse(models.Model):
    esp = models.OneToOneField(Esp, on_delete=models.CASCADE)
    numeroDeSalle = models.OneToOneField(ClasseNum, on_delete=models.CASCADE)
    def __str__(self):
        return 'Salle {} linked to {}'.format(self.numeroDeSalle, self.esp)

class SalleForm(ModelForm):
    class Meta:
        model = SalleDeClasse
        fields = '__all__'



