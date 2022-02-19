from django.shortcuts import render

from inventory.models import Inventory

def inventory(request):
	inventory_items = Inventory.objects.all();
	return render(request,'inventory/inventory.html', {'inventory_items': inventory_items})

def inventory_detail(request, id):
	inventory = Inventory.objects.get(id=id)
	return render(request,'inventory/inventory_detail.html', {'inventory': inventory})