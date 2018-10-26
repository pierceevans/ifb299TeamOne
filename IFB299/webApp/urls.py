from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView




urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('Customers/', views.CustomerListView.as_view(), name='customers'),
    path('Customers/<int:customerID>/', views.CustomerDetailView, name='customer-detail'),
    path('Car/<int:carID>/', views.CarDetailView, name='car-detail'),
    path('Store/<int:store_id>/', views.storeDetailView, name='store-detail'),
    path('Customers/<int:customerID>/Orders/<int:orderID>/', views.OrderDetailView, name='order-detail'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^all_cars/$', views.all_cars, name='all_cars'),
    url(r'^search_results/$', views.search_results, name='search_results'),
    url(r'^staff/portal/$', views.staffPortal, name='staff-portal'),
    url(r'^staff/customers/$', views.customerList, name='customer-list'),
    path('staff/customers/<int:customerID>/', views.CustomerDetailView, name='customer-detail-new'),
    url(r'^staff/orders/$', views.orderList, name='order-list'),
    url(r'^staff/reports/$', views.reportsView, name='reports'),
    url(r'^about-us/$', views.aboutView, name='about-us'),
    url(r'^store-map/$', views.mapView, name='store-map'),
]
