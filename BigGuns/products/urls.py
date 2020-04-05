from django.urls import path
from .views import ProductsListView
from . import views

urlpatterns = [
    path('',ProductsListView.as_view(), name = 'store-home')
]
