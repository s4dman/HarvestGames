from django.urls import path
from .views import home_view, details_view, products_view

app_name = 'personal'

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', products_view, name='products'),
    path('products/<slug>/', details_view, name='details')
]
