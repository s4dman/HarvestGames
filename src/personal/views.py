from django.shortcuts import render, get_object_or_404
from .models import Products

context = {}


def home_view(request):
    return render(request, "home.html")


def products_view(request, category):
    products = Products.objects.filter(category=category)
    first_product = Products.objects.filter(category=category)[:1].get()
    context['category'] = first_product.category
    context['products'] = products
    return render(request, "products.html", context)


def details_view(request, slug):
    model = Products
    product = get_object_or_404(Products, slug=slug)
    context['product'] = product
    return render(request, "details.html", context)
