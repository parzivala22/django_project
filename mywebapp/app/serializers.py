# mywebapp/core/serializers.py

from rest_framework import serializers
from .models import ProductMaster, ProductUpdateHistory, Job

class ProductMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaster
        fields = '__all__'

class ProductUpdateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUpdateHistory
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
