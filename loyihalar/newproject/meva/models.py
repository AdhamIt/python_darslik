from django.db import models

# Create your models here.
class Meva(models.Model):
    nomi=models.CharField(max_length=200)
    about=models.TextField()
    tami=models.CharField(max_length=200)
    rangi=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nomi