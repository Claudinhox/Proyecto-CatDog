from django.urls import path, include
from apps.product.views import ProductIndex, ProductAdd, ProductEdit, ProductDelete

urlpatterns = [
    path('product', ProductIndex, name="ProductIndex"),
    path('addproduct', ProductAdd, name="ProductAdd"),
    path('editproduct/<int:idProduct>',ProductEdit, name="ProductEdit"),
    path('deleteproduct/<int:idProduct>',ProductDelete, name="ProductDelete")
]