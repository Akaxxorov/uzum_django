from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/product-list.html', context=context)


def product_detali(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product
    }
    return render(request, 'products/product_detail.html',context=context)