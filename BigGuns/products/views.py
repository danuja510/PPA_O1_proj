from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product

class ProductsListView(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'

def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/home.html', context)

class ProductDetailView(DetailView):
    template_name = 'products/details.html'
    model = Product