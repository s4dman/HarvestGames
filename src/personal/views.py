from django.shortcuts import render


# Create your views here.

def home_view(request):
    print(request.headers)
    return render(request, "home.html", {})


def detail_view(request):
    return render(request, "base.html", {})