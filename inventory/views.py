import json

from django.shortcuts import render

import requests

def call_drf_api_endpoint(api):

	url = 'http://127.0.0.1:8000/' + api
	response = requests.get(url)
	json_data = response.json()

	return json_data


def inventory(request):
	# url = request.build_absolute_uri('/api/inventory')
	api = 'api/inventory/'
	inventory_items = call_drf_api_endpoint(api)

	return render(request,'inventory/inventory.html', {'inventory_items': inventory_items})

def inventory_detail(request, id):
	# url = request.build_absolute_uri(f'/api/inventory/{id}')
	api = f'api/inventory/{id}'
	inventory_items = call_drf_api_endpoint(api)

	return render(request,'inventory/inventory_detail.html', {'inventory': inventory})