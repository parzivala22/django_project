# mywebapp/core/views.py
# views.py

from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductMaster, ProductUpdateHistory, Job
from .serializers import ProductMasterSerializer, ProductUpdateHistorySerializer, JobSerializer
from .utils import navigate_asin_list, add_to_cart, view_product

# API Views
class ProductMasterListCreate(generics.ListCreateAPIView):
    queryset = ProductMaster.objects.all()
    serializer_class = ProductMasterSerializer

class ProductMasterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductMaster.objects.all()
    serializer_class = ProductMasterSerializer

class ProductUpdateHistoryListCreate(generics.ListCreateAPIView):
    queryset = ProductUpdateHistory.objects.all()
    serializer_class = ProductUpdateHistorySerializer

class ProductUpdateHistoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductUpdateHistory.objects.all()
    serializer_class = ProductUpdateHistorySerializer

class JobListCreate(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# Template Views
def product_list(request):
    products = ProductMaster.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

def product_detail(request, pk):
    product = ProductMaster.objects.get(pk=pk)
    return render(request, 'core/product_detail.html', {'product': product})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'core/job_list.html', {'jobs': jobs})

def asin_navigation(request):
    if request.method == 'POST':
        asin_list = ["B09HBVP5MX", "B09M88ZX3R", "B093PSR7KS"]
        navigate_asin_list(asin_list)
        return render(request, 'core/asin_navigation.html', {'message': 'ASIN navigation completed successfully.'})
    return render(request, 'core/asin_navigation.html')

def add_to_cart_view(request):
    if request.method == 'POST':
        asin_list = request.POST.getlist('asin_list')
        add_to_cart(asin_list)  # Call function to add to cart
        return JsonResponse({'message': 'Add to cart job started successfully.'})
    return render(request, 'add_to_cart.html')

def view_product_view(request):
    if request.method == 'POST':
        asin_list = request.POST.getlist('asin_list')
        view_product(asin_list)  # Call function to view product
        return JsonResponse({'message': 'View product job started successfully.'})
    return render(request, 'view_product.html')


