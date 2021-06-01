# Django
from django.shortcuts import render

def main(request):
    return render(request, 'accounts/base.html')