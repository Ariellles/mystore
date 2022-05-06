from django.shortcuts import render
from .models import Product
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, UpdateView, DeleteView


class ProductsListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'


class ContactUs(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('scontact')


class SuccessfulContact(TemplateView):
    template_name = 'successful_contact.html'


class HomePage(TemplateView):
    template_name = 'homepage.html'


class SuccessfulEdit(TemplateView):
    template_name = 'successful_update.html'


class SuccessfulAddition(TemplateView):
    template_name = 'successful_addition.html'


class SuccessfulDeletion(TemplateView):
    template_name = 'successful_deletion.html'


class Cart(TemplateView):
    template_name = 'cart.html'


class CreateProduct(CreateView):
    template_name = 'create_product.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('addition')


class EditProduct(UpdateView):
    template_name = 'edit_product.html'
    model = Product
    success_url = reverse_lazy('successful')
    context_object_name = 'product'
    fields = '__all__'


class DeleteProduct(DeleteView):
    template_name = 'delete_product.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('deletion')


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'

# Create your views here.
