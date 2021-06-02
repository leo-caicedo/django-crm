# Django
from django.urls import path

# Views
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>', views.customer, name="customer"),
]