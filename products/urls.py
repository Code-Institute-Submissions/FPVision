from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_products, name="all_products"),
    path("add_products/", views.add_product, name="add_products"),
    path(
        "edit_product/<int:product_id>",
        views.edit_product,
        name="edit_product"
    ),
    path(
        "delete_product/<int:product_id>",
        views.delete_product,
        name="delete_product"
    ),
    path(
        "<slug:category_slug>/",
        views.all_products,
        name="products_by_category"
    ),
    path(
        "<slug:category_slug>/<slug:subcategory_slug>/",
        views.all_products,
        name="products_by_subcategory",
    ),
    path(
        "<slug:category_slug>/<slug:subcategory_slug>/<slug:product_slug>",
        views.product_details,
        name="product_details",
    ),
]
