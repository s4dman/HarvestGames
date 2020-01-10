from django.shortcuts import render
from personal.models import Products


# Create your views here.

def home_view(request):
    return render(request, "home.html", {})


def details_view(request):
    context = {}
    products = Products.objects.all()
    context['products'] = products
    return render(request, "details.html", context)
