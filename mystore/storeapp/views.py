from django.shortcuts import render
from .models import Product
from .forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, UpdateView


class ProductsListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'


class ContactUs(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('products')


class HomePage(TemplateView):
    template_name = 'homepage.html'


class CreateProduct(CreateView):
    template_name = 'create_product.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('homepage')


class EditProduct(UpdateView):
    template_name = 'edit_product.html'
    model = Product
    success_url = reverse_lazy('homepage')
    context_object_name = 'product'
    fields = '__all__'

# Create your views here.
