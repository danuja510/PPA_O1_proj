from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class ProductsListView(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'posts'

products = [
    {
        'title': 'BigGun',
        'type': 'LMG',
        'description': 'Large Machine Gun',
        'date_posted': 'April 05, 2020',
        'price': 499.99,
        'stock':5,
        'image': 'gun.jpg',
        'manufacturer': 'mn'
    },
    {
        'title': 'BigGun2',
        'type': 'SMG',
        'description': 'Small Machine Gun',
        'date_posted': 'April 05, 2020',
        'price': 399.99,
        'stock':6,
        'image': 'gun2.jpg',
        'manufacturer': 'mn'
    },
    {
        'title': 'BigGun3',
        'type': 'MG',
        'description': 'Machine Gun',
        'date_posted': 'April 05, 2020',
        'price': 299.99,
        'stock':4,
        'image': 'gun3.png',
        'manufacturer': 'mn'
    },
    {
        'title': 'BigGun3',
        'type': 'MG',
        'description': 'Machine Gun',
        'date_posted': 'April 05, 2020',
        'price': 299.99,
        'stock':4,
        'image': 'gun3.png',
        'manufacturer': 'mn'
    },
    {
        'title': 'BigGun3',
        'type': 'MG',
        'description': 'Machine Gun',
        'date_posted': 'April 05, 2020',
        'price': 299.99,
        'stock':4,
        'image': 'gun3.png',
        'manufacturer': 'mn'
    },
    {
        'title': 'BigGun3',
        'type': 'MG',
        'description': 'Machine Gun',
        'date_posted': 'April 05, 2020',
        'price': 299.99,
        'stock':4,
        'image': 'gun3.png',
        'manufacturer': 'mn'
    },
    {
        'title': 'BigGun3',
        'type': 'MG',
        'description': 'Machine Gun',
        'date_posted': 'April 05, 2020',
        'price': 299.99,
        'stock':4,
        'image': 'gun3.png',
        'manufacturer': 'mn'
    },
    {
        'title': 'BigGun3',
        'type': 'MG',
        'description': 'Machine Gun',
        'date_posted': 'April 05, 2020',
        'price': 299.99,
        'stock':4,
        'image': 'gun3.png',
        'manufacturer': 'mn'
    }
]

def home(request):
    context = {
        'products': products
    }
    return render(request, 'products/home.html', context)
