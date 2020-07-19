from django.urls import path
from .views import home_view, details_view, products_view, products_category_view

app_name = 'personal'

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', products_view, name='products'),
    path('products/<category>', products_category_view, name='products'),
    path('products/<str:slug>/', details_view, name='details')
]
