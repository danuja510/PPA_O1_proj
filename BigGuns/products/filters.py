from . models import Product
import django_filters

# Creating product filters
class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Product
        fields = ['title']