from django.contrib import admin

from store.models import Product
from store.views import products

admin.site.register(Product)