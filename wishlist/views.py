from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Wishlist
from products.models import Product

@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})

@login_required
def add_to_wishlist(request, product_id):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=product_id)
    wishlist.products.add(product)
    return redirect('wishlist:wishlist_view')

@login_required
def remove_from_wishlist(request, product_id):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=product_id)
    wishlist.products.remove(product)
    return redirect('wishlist:wishlist_view')
