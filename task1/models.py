from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    balance = models.FloatField()
    age = models.IntegerField()



class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.FloatField()
    size = models.FloatField()
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')


class Basket(models.Model):
    Buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='basket')

    def __str__(self):
        return f'Корзина для {self.Buyer.name}'


