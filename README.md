# Inventory Management


## Installation:

1. Install the requirements
`pip instal -r requirements.txt`

2. Run the server
`python manage.py runserver`

## Run tests:
`python manage.py test`

## Constraints:
When using drf api end point to get data for `/inventory` view, unit tests would fail when determining the URL dynamically as follows:
`url = request.build_absolute_uri('/api/inventory')`

Instead, if the absolute URL is used, then the tests pass:
`url = 'http://127.0.0.1:8000/api/inventory/'`