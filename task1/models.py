from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.FloatField()
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.FloatField()
    size = models.FloatField()
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
