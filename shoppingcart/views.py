from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

# Add this new view function
def cart_detail(request):
    """
    Displays the contents of the shopping cart.
    Fetches cart items dynamically and calculates the total.
    """
    cart_items = request.session.get('cart', {})
    items = []
    total = 0

    for product_id, quantity in cart_items.items():
        product = get_object_or_404(Product, id=product_id)
        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })
        total += product.price * quantity

    return render(request, 'shoppingcart/cart_detail.html', {
        'cart_items': items,
        'total': total
    })


# Add to Cart
def add_to_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        print(f"Add {quantity} of product {product_id} to cart")
        messages.success(request, f'Added {quantity} of product {product_id} to cart.')
        # Consider redirecting to the cart_detail page instead of home
        return redirect('shoppingcart:cart_detail') # Or 'home' if that's preferred


# Cash on Delivery View
def cash_on_delivery(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        lane = request.POST.get('lane')
        building = request.POST.get('building')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        quantity = int(request.POST.get('quantity', 1))

        if all([name, phone, lane, building, city, state, pincode]):
            full_address = f"{name}, {phone}, {building}, {lane}, {city}, {state} - {pincode}"
            messages.success(request, f'✅ Order placed for {quantity} x "{product.name}" to: {full_address}')
            return redirect('products:product_list')
        else:
            messages.error(request, '❌ All address fields are required.')

    return render(request, 'shoppingcart/cash_on_delivery.html', {'product': product})


    
# These views can remain in case you switch back to Stripe or need them
def payment_success(request):
    return render(request, 'cart/success.html')

def payment_cancel(request):
    return render(request, 'cart/cancel.html')


# Keep only if you're still using Stripe
"""
import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_now(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100),  # cents
            },
            'quantity': quantity,
        }],
        mode='payment',
        success_url=settings.DOMAIN + '/cart/success/',
        cancel_url=settings.DOMAIN + '/cart/cancel/',
    )

    return redirect(session.url, code=303)
"""