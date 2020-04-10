from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product
from .filters import ProductFilter

class ProductsListView(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/home.html', context)

class ProductDetailView(DetailView):
    template_name = 'products/details.html'
    model = Product