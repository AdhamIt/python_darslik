from django.db import models

# Create your models here.
class Kitop(models.Model):
    nomi=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    tili=models.CharField(max_length=200)
    bet_soni=models.IntegerField()
    narxi=models.IntegerField()

    def __str__(self) -> str:
        return self.nomi

