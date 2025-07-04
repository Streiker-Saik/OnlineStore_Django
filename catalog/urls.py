from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig

from .views import (ContactsCreateView, ProductCreateViews, ProductDeleteViews, ProductDetailViews, ProductsListViews,
                    ProductUpdateViews, PublishProductViews)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListViews.as_view(), name="home"),
    path("contacts/", ContactsCreateView.as_view(), name="contacts"),
    path("product/<int:pk>/detail/", ProductDetailViews.as_view(), name="product_detail"),
    path("product/create/", ProductCreateViews.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateViews.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", ProductDeleteViews.as_view(), name="product_delete"),
    path("product/<int:pk>/unpublish/", PublishProductViews.as_view(), name="product_unpublish"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
