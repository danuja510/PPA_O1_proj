from django.urls import path
from .views import ProductsListView, ProductDetailView
from . import views
from cart.views import add_to_cart, remove_from_cart

urlpatterns = [
    path('',views.home, name = 'store-home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-details'),
    path('cart/<id>', add_to_cart, name='cart'),
    path('remove/<id>', remove_from_cart, name='remove-cart'),
]

