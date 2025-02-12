from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    generic_name = models.CharField(max_length=100, blank=True, null=True)
    quantity_available = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_out_of_stock = models.BooleanField(default=False)
    price_per_unit = models.BooleanField(default=False,
                                         help_text="Indicates if the price is per unit (e.g., tablet, ampoule) "
                                                   "or for the full product.")
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand_name or self.generic_name} - {self.category.name}"

    class Meta:
        ordering = ['category', 'brand_name']