from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


class Market(models.Model):
    name = models.CharField(max_length=200)
    ratings = GenericRelation(Rating, related_query_name='markets')
    photo = models.CharField(max_length=190000)

    def __str__(self):
        return self.name
