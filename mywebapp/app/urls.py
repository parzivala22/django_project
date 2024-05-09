# mywebapp/core/urls.py

# mywebapp/core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URLs for Task 1 (Template Views)
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('jobs/', views.job_list, name='job-list'),
    path('navigate-asin/', views.asin_navigation, name='navigate-asin'),

    # URLs for Task 2 (CRUD APIs)
    path('api/products/', views.ProductMasterListCreate.as_view(), name='api-product-list'),
    path('api/products/<int:pk>/', views.ProductMasterRetrieveUpdateDestroy.as_view(), name='api-product-detail'),
    path('api/product-updates/', views.ProductUpdateHistoryListCreate.as_view(), name='api-product-update-list'),
    path('api/product-updates/<int:pk>/', views.ProductUpdateHistoryRetrieveUpdateDestroy.as_view(),
         name='api-product-update-detail'),
    path('api/jobs/', views.JobListCreate.as_view(), name='api-job-list'),
    path('api/jobs/<int:pk>/', views.JobRetrieveUpdateDestroy.as_view(), name='api-job-detail'),
]
