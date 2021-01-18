from django.db import models
from django.contrib.auth.models import AbstractUser


class Profiel(AbstractUser):
    bedrijfsnaam = models.CharField(max_length=300,blank=True)
    omschrijving = models.TextField(max_length=500,blank=True)
    contactpersoon = models.CharField(max_length=200, blank=True)
    straatnaam = models.CharField(max_length=300, blank=True)
    postcode = models.CharField(max_length=7, blank=True)
    plaats = models.CharField(max_length=100, blank=True)
    telefoonnummer = models.CharField(max_length=15, blank=True)
    website = models.URLField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='logos',blank=True)
    foto = models.ImageField(upload_to='fotos',blank=True)

