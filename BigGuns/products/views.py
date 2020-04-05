from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class ProductsListView(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'posts'

def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/home.html', context)
