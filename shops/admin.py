from django.contrib import admin
from .models import Shop, Category, Product, ProductsImages

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductsImages)
