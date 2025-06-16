from django.urls import path

from catalog.apps import CatalogConfig

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product_detail/<int:pk>/detail/', views.product_detail, name='product_detail'),
    path('product_add', views.product_add, name='product_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
