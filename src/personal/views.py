from django.shortcuts import render
from personal.models import Products

# Create your views here.

context = {}
products = Products.objects.all()


def home_view(request):
    return render(request, "home.html", context)


def products_view(request):
    context['products'] = products
    return render(request, "products.html", context)


def details_view(request):
    context['products'] = products
    return render(request, "details.html", context)
