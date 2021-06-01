# Django
from django.urls import path

# Views
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
]