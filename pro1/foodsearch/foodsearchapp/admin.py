from django.contrib import admin
from .models import Product, Toppings, ToppingsGroups, ProductToppings, Rating,ProductCategory

admin.site.register(Product)
admin.site.register(Toppings)
admin.site.register(ToppingsGroups)
admin.site.register(ProductToppings)
admin.site.register(Rating)
admin.site.register(ProductCategory)