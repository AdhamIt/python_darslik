from django.db import models

# Create your models here.
class Book(models.Model):
    nomi=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    betsoni=models.IntegerField()
    til=models.CharField(max_length=10)
    about=models.TextField()

    def __str__(self) -> str:
        return self.nomi + "  "+ self.author
