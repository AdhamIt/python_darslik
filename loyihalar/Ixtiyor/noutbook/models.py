from django.db import models

# Create your models here.
class Noutbook(models.Model):
    nomi=models.CharField(max_length=200)
    about=models.CharField(max_length=200)
    # nm= models.