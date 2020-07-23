from django.db import models

# Create your models here.
from django.urls import reverse_lazy
from django.utils.text import slugify

AVAILABILITY = [
    ("In Stock", "in-stock"),
    ("Out Of Stock", "out-of-stock")
]


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_slug = models.SlugField(blank=True, unique=True)

    def get_absolute_url(self):
        return reverse_lazy('details', kwargs={'product_category': self.name})

    def save(self, *args, **kwargs):
        value = self.name
        self.category_slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Products(models.Model):
    title = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    availability = models.CharField(max_length=20, choices=AVAILABILITY)
    slug = models.SlugField(blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='category_slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('details', kwargs={'product_slug': self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
