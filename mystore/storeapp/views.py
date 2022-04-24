from django.shortcuts import render
from .models import Product
from django.views.generic import TemplateView, ListView, DetailView, CreateView


class ProductsListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'


class ContactUs(CreateView):
    template_name = 'contact.html'
    context_object_name = 'contact'


class HomePage(TemplateView):
    template_name = 'homepage.html'


class CreateProduct(CreateView):
    template_name = 'create_product.html'
    model = Product
    fields = '__all__'

# Create your views here.
