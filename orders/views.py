from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Order

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})

@login_required
def checkout(request):
    # This is a placeholder for the checkout logic
    if request.method == 'POST':
        # Process order creation here
        # ...
        return redirect('orders:order_history')
    return render(request, 'orders/checkout.html')
