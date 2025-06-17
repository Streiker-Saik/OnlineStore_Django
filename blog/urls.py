from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig

from .views import BlogCreateView, BlogDeleteViews, BlogDetailViews, BlogListViews, BlogUpdateViews

app_name = CatalogConfig.name

urlpatterns = [
    path('blog/', BlogListViews.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('product/<int:pk>/detail/', BlogDetailViews.as_view(), name='blog_detail'),
    path('product/<int:pk>/delete/', BlogDeleteViews.as_view(), name='blog_delete'),
    path('product/<int:pk>/update/', BlogUpdateViews.as_view(), name='blog_update'),
]