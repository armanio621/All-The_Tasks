from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)       # Name of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price
    description = models.TextField(blank=True)     # Optional description
    image = models.URLField()                      # Image from internet (remote URL or local static path)
    local_image = models.CharField(max_length=255, blank=True)  # optional local static path

    def __str__(self):
        return self.title
