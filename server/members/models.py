from django.db import models
from django.db.models.base import Model

# Create your models here.

class Position(models.Model):
    position = models.CharField(max_length=30)

    def __str__(self):
        return self.position

class Member(models.Model):
    name = models.CharField(max_length=5)
    e_name = models.CharField(max_length=10)
    age = models.IntegerField()
    birth = models.DateField()
    youtube = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200)
    profile = models.URLField(max_length=200)
    position = models.ManyToManyField(Position)

    def __str__(self):
        return self.name