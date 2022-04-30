from django.db import models

# Create your models here.
class Uquvchi(models.Model):
    ism=models.CharField(max_length=200)
    fam=models.CharField(max_length=200)
    otasi=models.CharField(max_length=200)
    yoshi=models.IntegerField()
    sinfi=models.IntegerField()

    def __str__(self) -> str:
        return self.nomi