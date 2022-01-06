from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=1000)
    weight = models.DecimalField(max_digits=2,decimal_places=2)
    price = models.DecimalField(max_digits=2,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'products'
