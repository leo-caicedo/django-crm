# Django
from django.urls import path

# Views
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user_page, name='user_page'),

    path('accounts/', views.account_settings, name='account'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('products/', views.products, name='products'),
    path('customer/<str:pk>', views.customer, name='customer'),

    path('create_order/<str:pk>', views.create_order, name='create_order'),
    path('update_order/<str:pk>', views.update_order, name='update_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),
]
