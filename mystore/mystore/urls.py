"""mystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from storeapp.views import ProductsListView
from storeapp.views import ContactUs
from storeapp.views import HomePage
from storeapp.views import CreateProduct
from storeapp.views import EditProduct
from storeapp.views import DeleteProduct
from storeapp.views import ProductDetail
from storeapp.views import SuccessfulEdit
from storeapp.views import SuccessfulAddition
from storeapp.views import SuccessfulDeletion
from storeapp.views import SuccessfulContact


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop', ProductsListView.as_view(), name='products'),
    path('contact', ContactUs.as_view(), name='contact'),
    path('', HomePage.as_view(), name= 'homepage'),
    path('create', CreateProduct.as_view(), name='create'),
    path('products/<int:pk>/edit', EditProduct.as_view(), name='edit'),
    path('products/<int:pk>/delete', DeleteProduct.as_view(), name='delete_product'),
    path('products/<int:pk>/add', DeleteProduct.as_view(), name='add_product'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('successful', SuccessfulEdit.as_view(), name='successful'),
    path('addition', SuccessfulAddition.as_view(), name='addition'),
    path('deletion', SuccessfulDeletion.as_view(), name= 'deletion'),
    path('scontact', SuccessfulContact.as_view(),name= 'scontact')

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
