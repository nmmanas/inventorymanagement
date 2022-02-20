import json

from django.shortcuts import render

import requests

def call_drf_api_endpoint(request, api):
	url = request.build_absolute_uri(api)
	response = requests.get(url)
	json_data = response.json()

	return json_data


def inventory(request):
	api = '/api/inventory/'
	inventory_items = call_drf_api_endpoint(request, api)

	return render(request,'inventory/inventory.html', {'inventory_items': inventory_items})

def inventory_detail(request, id):
	api = f'/api/inventory/{id}'
	inventory = call_drf_api_endpoint(request, api)

	return render(request,'inventory/inventory_detail.html', {'inventory': inventory})