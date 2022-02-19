from rest_framework import viewsets

from inventory.api.serializers import SupplierSerializer, InventorySerializer
from inventory.models import Supplier, Inventory


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer