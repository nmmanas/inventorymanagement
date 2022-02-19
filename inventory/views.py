import json

from django.shortcuts import render

import requests

def inventory(request):
	url = request.build_absolute_uri('/api/inventory')
	response = requests.get(url)
	inventory_items = response.json()

	return render(request,'inventory/inventory.html', {'inventory_items': inventory_items})

def inventory_detail(request, id):
	url = request.build_absolute_uri(f'/api/inventory/{id}')
	response = requests.get(url)
	inventory = response.json()
	
	return render(request,'inventory/inventory_detail.html', {'inventory': inventory})