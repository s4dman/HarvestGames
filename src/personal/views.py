from django.shortcuts import render, get_object_or_404
from .models import Products

context = {}


def home_view(request):
    return render(request, "home.html")


def products_view(request):
    products = Products.objects.all()
    context['products'] = products
    return render(request, "products.html", context)


def details_view(request, slug):
    product = get_object_or_404(Products, slug=slug)
    context['product'] = product
    return render(request, "details.html", context)
