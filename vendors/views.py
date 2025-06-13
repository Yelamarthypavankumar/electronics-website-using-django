from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Vendor, VendorProduct
from products.models import Product

@login_required
def dashboard(request):
    vendor = Vendor.objects.filter(user=request.user).first()
    if not vendor:
        return redirect('vendors:register')
    products = VendorProduct.objects.filter(vendor=vendor)
    return render(request, 'vendors/dashboard.html', {'vendor': vendor, 'products': products})

@login_required
def register(request):
    # Placeholder for vendor registration logic
    return render(request, 'vendors/register.html')
