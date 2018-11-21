from django.contrib import admin
from .models import Product
from .models import Historic

admin.site.register(Product)
admin.site.register(Historic)

# Register your models here.
