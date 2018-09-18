from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('', views.index, name='index'),
    path('Customers/', views.CustomerListView.as_view(), name='customers'),
    path('Customers/customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('Orders/', views.OrderListView.as_view(), name='orders'),
]