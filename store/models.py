from django.db import models

class Customer(models.Model):
    name = models.TextField(max_length=50)
    address = models.TextField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.TextField(max_length=50)
    unit_price = models.FloatField()
    description = models.TextField(max_length=100, default="This is the description. Click to")
    image = models.ImageField(null=True)
    code = models.TextField(max_length=16, null=True, default="N/A", blank=True)
    def __str__(self):
        return self.title