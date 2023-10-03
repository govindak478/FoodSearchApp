from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    product_category = models.CharField(max_length=100)
    veg_non_veg = models.CharField(max_length=8, choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')])
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'foodsearchapp_product'

class ProductCategory(models.Model):
    # Define fields for ProductCategory as needed
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Toppings(models.Model):
    topping_id = models.AutoField(primary_key=True)
    group_id = models.IntegerField()
    topping_name = models.CharField(max_length=100)
    categories = models.ManyToManyField(ProductCategory, related_name='toppings')

    def __str__(self):
        return self.topping_name

class ToppingsGroups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name

class ProductToppings(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    topping = models.ForeignKey(Toppings, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.product_name} - {self.topping.topping_name}"

class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating_value = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.product.product_name} - {self.rating_value}"

    class Meta:
        db_table = 'foodsearchapp_rating'  # Specify the table name

