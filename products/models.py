from django.db import models
from markets.models import Market
from users.models import CustomUser

class Historic (models.Model):
    price = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    commerce = models.ForeignKey('markets.Market', models.DO_NOTHING)
    points = models.IntegerField(default=0)
    def _self_(self):
        return self.price


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    photo = models.CharField(max_length=190000)
    historic = models.ManyToManyField(Historic)

    def _self_(self):
        return self.description


class ShoppingList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)