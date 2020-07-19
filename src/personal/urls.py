from django.urls import path
from .views import home_view, details_view, products_view

app_name = 'personal'

urlpatterns = [
    path('', home_view, name='home'),
    path('<str:category>/', products_view, name='products'),
    path('product/<str:slug>/', details_view, name='details')
]
