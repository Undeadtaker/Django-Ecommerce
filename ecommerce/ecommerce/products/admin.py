from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import Product, Category, ProductImage

# Register your models here.
admin.site.register(Category, MPTTModelAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]

