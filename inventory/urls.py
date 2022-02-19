from django.urls import include, re_path
from rest_framework import routers

from . import views 
from inventory.api import views as api

router = routers.DefaultRouter()
router.register(r'inventory', api.InventoryViewSet)

app_name = "inventory"

urlpatterns = [
    re_path(r'^api/', include(router.urls)),
    re_path(r'^inventory/$', views.inventory),
    re_path(r'^inventory/(\d+)/$', views.inventory_detail, name="detail"),
]