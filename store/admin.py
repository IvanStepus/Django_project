from django.contrib import admin
from .models import Product, Cart


# Register your models here.

#
# admin.site.register(Product) #1st
#
# class ProductAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Product, ProductAdmin)   #2nd

@admin.action(description='Sale to 20')
def make_published(modeladmin, request, queryset):
    queryset.update(sale_count=0.8, sale=True)

@admin.action(description='Sale Off')
def sale_off(modeladmin, request, queryset):
    queryset.update(sale_count=1, sale=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):     # 3rd
    list_display = ['title', 'current_price', 'created_at', 'sale']
    list_filter = ["created_at"]
    search_fields = ['title']
    actions = [make_published, sale_off]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass
    # list_display = ['title', 'current_price', 'created_at', 'sale']
    # list_filter = ["created_at"]
    # search_fields = ['title']
    # actions = [make_published, sale_off]