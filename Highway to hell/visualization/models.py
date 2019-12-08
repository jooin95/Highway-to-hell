
from djongo import models
from django import forms
from jsonfield import JSONField
from django.contrib.postgres.fields import ArrayField
# Create your models here.



class CastTest(models.Model):
    zdate = models.DateTimeField(null=True)
    zcharge = models.CharField(max_length=100, null=True)
    zprowe = models.FloatField(null=True)
    zbadwe = models.FloatField(null=True)
