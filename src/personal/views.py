from django.shortcuts import render, get_object_or_404
from personal.models import Products

# Create your views here.

context = {}


def home_view(request):
    return render(request, "home.html")


def products_view(request):
    products = Products.objects.all()
    context['products'] = products
    return render(request, "products.html", context)


def details_view(request, slug):
    products = get_object_or_404(Products, slug=slug)
    context['products'] = products
    return render(request, "details.html", context)
