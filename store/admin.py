from django.contrib import admin
from .models import *





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


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['title']

@admin.register(Supermarket)
class SupermarketAdmin(admin.ModelAdmin):
    pass
