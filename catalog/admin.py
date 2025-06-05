from django.contrib import admin
from .models import Category, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для работы администратора с категориями"""
    list_display = ("id", "name",)
    search_fields = ("name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для работы администратора с продуктами"""
    list_display = ("id", "name", "price", "category",)
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Класс для работы администратора с контактами"""
    list_display = ("name", "phone", "message",)
    list_filter = ("created_at",)
    ordering = ("name",)