# Django
from django.urls import path

# Views
from accounts.views import main

app_name = 'accounts'
urlpatterns = [
    path('', main),
]