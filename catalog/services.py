from typing import Callable

from django.core.cache import cache
from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from config.settings import CACHE_ENABLED
from users.models import CustomUser

from .models import Product, Category


class DecoratorsService:
    """
    Сервисный класс для работы с декораторами
    Методы:
        get_cache_decorator(cached_enable: bool = CACHE_ENABLED) -> Callable:
            Возвращает декоратор для кеширования.
    """

    @staticmethod
    def get_cache_decorator(cached_enable: bool = CACHE_ENABLED) -> Callable:
        """
        Возвращает декоратор для кеширования.
        :param cached_enable: Включение кеширования.
        :return: Декоратор для кеширования.
        """
        if cached_enable:
            cache_decorator = method_decorator(cache_page(60 * 15), name="dispatch")
        else:
            cache_decorator = lambda view: view
        return cache_decorator


class ProductService:
    """
    Сервисный класс работы с продуктами
    Методы:
        get_products_by_category(category_id: int) -> QuerySet[Product]:
            Возвращает список всех продуктов в указанной категории.
        get_products_from_cache() -> QuerySet[Product]:
            Возвращает данные по продуктам из кэша, если кэш пуст, получает данные из БД.
        filter_products_by_permission(products: QuerySet, user: CustomUser) -> QuerySet:
            Фильтрация продуктов по правам пользователя.
    """

    @staticmethod
    def get_products_by_category(category_id: int) -> QuerySet[Product]:
        """
        Возвращает список всех продуктов в указанной категории.
        :param category_id: ID категории.
        :return: QuerySet продуктов в указанной категории.
        """
        products = Product.objects.filter(category_id=category_id)
        return products

    @staticmethod
    def get_products_from_cache() -> QuerySet[Product]:
        """
        Возвращает данные по продуктам из кэша, если кэш пуст, получает данные из БД.
        :return: QuerySet продуктов из кэша
        """

        if not CACHE_ENABLED:
            return Product.objects.all()
        key = "product_list"
        products = cache.get(key)
        if products is None:
            products = Product.objects.all()
            cache.set(key, products)
        return products

    @staticmethod
    def filter_products_by_permission(products: QuerySet, user: CustomUser) -> QuerySet:
        """
        Фильтрация продуктов по правам пользователя.
        :param products: QuerySet продуктов для фильтрации.
        :param user: Пользователь, права которого проверяются.
        :return: QuerySet отфильтрованных продуктов.
        """

        if not (user.has_perm("catalog.can_unpublish_product") or user.is_superuser):
            products = products.filter(publication=True)
        return products


class CategoryService:
    """
    Сервисный класс работы с категориями
    Методы:
        get_all_categories() -> QuerySet:
            Возвращает список всех продуктов в указанной категории.
    """

    @staticmethod
    def get_all_categories() -> QuerySet:
        """
        Получает все категории, отсортированные по названию.
        :return: QuerySet продуктов из кэша
        """
        categories = Category.objects.all().order_by('name')
        return categories