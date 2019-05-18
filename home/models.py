from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Data(models.Model):
    ad_soyad = models.CharField(max_length=1500, null=True, blank=True)
    yasadigi_region = models.CharField(max_length=1500, null=True, blank=True)
    profili = models.CharField(max_length=1500, null=True, blank=True)
    elaqenomresi = models.CharField(max_length=1500, null=True, blank=True)
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    problemler = models.CharField(max_length=1500, null=True, blank=True)
    veziyyetsablonu = models.CharField(max_length=1500, null=True, blank=True)
    seher = models.CharField(max_length=1500, null=True, blank=True)
    kend = models.CharField(max_length=1500, null=True, blank=True)

    def __str__(self):
        return self.ad_soyad
