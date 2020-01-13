from django.db import models

# Create your models here.
from django.urls import reverse_lazy

AVAILABILITY = [
    ("In Stock", "in-stock"),
    ("Out Of Stock", "out-of-stock")
]


class Products(models.Model):
    title = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    availability = models.CharField(max_length=20, choices=AVAILABILITY)

    def get_absolute_url(self):
        return reverse_lazy('details', kwargs={'product_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
