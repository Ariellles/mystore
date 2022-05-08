from django.shortcuts import render
from .models import Product, Purchase
from .forms import ContactForm, PurchaseForm, RegisterUserForm
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


class SuccessfulPurchase(TemplateView):
    template_name = 'successful_purchase.html'


class PurchaseView(LoginRequiredMixin, FormView):
    template_name = 'purchase.html'
    success_url = reverse_lazy('payment')
    form_class = PurchaseForm

    def get_context_data(self, **kwargs):
        product = Product.objects.get(id=self.kwargs['pk'])
        context = super(PurchaseView,self).get_context_data(**kwargs)
        context['product'] = product
        return context

    def get_initial(self):
        initial = super(PurchaseView, self).get_initial()
        product = Product.objects.get(id=self.kwargs['pk'])

        initial.update({'product': product.pk})
        return initial

    def form_valid(self, form):
        form.save()
        return super(PurchaseView, self).form_valid(form)


class CreateProduct(PermissionRequiredMixin, CreateView):
    template_name = 'create_product.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('addition')
    permission_required = 'viewer.create_product'


class EditProduct(PermissionRequiredMixin, UpdateView):
    template_name = 'edit_product.html'
    model = Product
    success_url = reverse_lazy('successful')
    context_object_name = 'product'
    fields = '__all__'
    permission_required = 'viewer.edit_product'


class DeleteProduct(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_product.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('deletion')
    permission_required = 'viewer.delete_product'


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'


class RegisterUser(CreateView):
    template_name = 'register_user.html'
    success_url = reverse_lazy('products')
    form_class = RegisterUserForm

# Create your views here.
