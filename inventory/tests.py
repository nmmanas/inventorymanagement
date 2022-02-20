from django.test import TestCase, Client
from django.urls import reverse

from unittest.mock import patch

from inventory.models import Inventory, Supplier

class InventoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 10 items
        number_of_items = 10

        supplier = Supplier.objects.create(name='sup')

        for item_id in range(number_of_items):
            Inventory.objects.create(
                name=f'name {item_id}',
                description=f'description {item_id}',
                note=f'note {item_id}',
                stock=10,
                availability=True,
                supplier= supplier,
            )

    @patch("inventory.views.call_drf_api_endpoint", autospec=True)
    def test_inventory_list_url(self, mock_call_drf_api_endpoint):
        url = reverse('inventory:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    @patch("inventory.views.call_drf_api_endpoint", autospec=True)
    def test_inventory_detail_url(self, mock_call_drf_api_endpoint):
        url = reverse('inventory:detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_inventory_api_url(self):
        url = '/api/inventory/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
