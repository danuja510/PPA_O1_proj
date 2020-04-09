from django.urls import path
from .views import ProductsListView, ProductDetailView
from . import views
from cart.views import add_to_cart, remove_from_cart, CartView, decreaseCart, checkout

urlpatterns = [
    path('',views.home, name = 'store-home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-details'),
    path('add/<id>', add_to_cart, name='add-cart'),
    path('remove/<id>', remove_from_cart, name='remove-cart'),
    path('cart', CartView, name='view-cart'),
    path('decrease/<id>', decreaseCart, name='decrease-cart'),
    path('checkout/', checkout, name='checkout'),
]

