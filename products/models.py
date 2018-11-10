from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    commerce = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    photo = models.CharField(max_length=190000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _self_(self):
        return self.description
