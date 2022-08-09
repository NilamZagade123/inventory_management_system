from django.test import TestCase

# Create your tests here.
from .models import Supplier, Inventory

class InventoryAPITestCases(TestCase):
    def setUp(self):
        supplier_object = Supplier.objects.create(name="Nilam")
        Inventory.objects.create(name="inv1",description="desc",note="inventory note",supplier=supplier_object)
       

    def test_inventory_api(self):
        #test case to check “/inventory” url is returns "200 OK status" or not
        response = self.client.get("/inventory")    
        self.assertEqual(response.status_code, 200)

        #test case to check “/api/inventory” url is returns "200 OK status" or not
        inventoryresponse = self.client.get("/api/inventory")    
        self.assertEqual(inventoryresponse.status_code, 200)

        #test case to check “/inventory/<id>” url is returns "200 OK status" or not
        response = self.client.get("/inventory/1")  
        self.assertEqual(response.status_code, 200)

        

        