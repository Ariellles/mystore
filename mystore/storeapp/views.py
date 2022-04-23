from django.shortcuts import render
from .models import Product
from django.views.generic import TemplateView, ListView, DetailView


class ProductsListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'


# Create your views here.
