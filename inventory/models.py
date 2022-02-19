from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=100, blank=True, default='')
    note = models.CharField(max_length=200, blank=True, default='')
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey(Supplier, related_name='inventory', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Inventories"