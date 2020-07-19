from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Products

context = {}


def home_view(request):
    return render(request, "home.html")


def all_products_view(request):
    try:
        products = Products.objects.all()
        context['products'] = products
        return render(request, "products.html", context)
    except Products.DoesNotExist:
        return render(request, "404.html")


def products_view(request, category):
    products = get_list_or_404(Products, category=category)
    first_product = Products.objects.filter(category=category)[:1].get()
    context['category'] = first_product.category
    context['products'] = products
    return render(request, "products.html", context)


def details_view(request, slug):
    product = get_object_or_404(Products, slug=slug)
    context['product'] = product
    return render(request, "details.html", context)
