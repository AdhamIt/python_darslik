from django.db import models

# Create your models here.
class Maktab(models.Model):
    nomi=models.CharField(max_length=200)
    manzili=models.CharField(max_length=200)
    uquvchi_soni=models.IntegerField()
    about=models.TextField()

    def __str__(self) -> str:
        return self.nomi
