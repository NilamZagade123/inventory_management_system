from django.contrib import admin

# Register your models here.
from .models import Supplier,Inventory

# Register Supplier and Inventory models
admin.site.register(Supplier)
admin.site.register(Inventory)