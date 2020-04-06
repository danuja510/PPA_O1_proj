from django.urls import path
from .views import ProductsListView, ProductDetailView
from . import views

urlpatterns = [
    path('',views.home, name = 'store-home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-details')
]
