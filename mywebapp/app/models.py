# mywebapp/core/models.py

from django.db import models

class ProductMaster(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    asin = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductUpdateHistory(models.Model):
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    previous_attribute = models.CharField(max_length=100)
    current_attribute = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product} - {self.created_at}"

class Job(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    total_count = models.IntegerField(default=0)
    current_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
