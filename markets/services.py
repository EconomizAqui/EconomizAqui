import types
import operator
from .models import Market

class MarketSorter:  
    def __init__(self, func=None):
        self.queryset = list(Market.objects.all())
        if func is not None:
            self.sort = types.MethodType(func, self)

    def sort(self):
        return self.queryset

    def sort_by_name_ascending(self):
        return Market.objects.order_by('name')

    def sort_by_name_descending(self):
        return Market.objects.order_by('name').reverse

    def sort_by_rating_ascending(self):
        return Market.objects.filter(ratings__isnull=False).order_by('ratings__average').reverse()

    def sort_by_rating_descending(self):
        return Market.objects.filter(ratings__isnull=False).order_by('ratings__average')
