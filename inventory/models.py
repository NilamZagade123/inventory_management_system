# import the standard Django Model
# from built-in library
from django.db import models

import django
# declare a new model with a name "Supplier"
class Supplier(models.Model):
    
    name = models.CharField(max_length=255,unique=True)

    # renames the instances of the model
    # with their  name
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'supplier'

# declare a new model with a name "Inventory"
class Inventory(models.Model):
    name = models.CharField(max_length=255, null=True,)
    description = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True, default=0)
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, 
                                  related_name='get_supplier_details')

    # renames the instances of the model
    # with their  name
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'inventory'