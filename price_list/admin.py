from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'generic_name', 'quantity_available', 'price',
                    'is_out_of_stock', 'price_per_unit', 'category')
    list_filter = ('category', 'is_out_of_stock', 'price_per_unit')
    search_fields = ('brand_name', 'generic_name', 'category__name')
    list_editable = ('price', 'quantity_available', 'is_out_of_stock')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

# Register models with their respective admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
