from django.db import models

# Create your models here.
class Telefon(models.Model):
    modeli=models.CharField(max_length=200)
    narxi=models.IntegerField()

    def __str__(self) -> str:
        return self.modeli