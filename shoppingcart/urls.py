# shoppingcart/urls.py
from django.urls import path
from . import views

app_name = 'shoppingcart'

urlpatterns = [
    # Add this line to handle the base /shoppingcart/ URL
    path('', views.cart_detail, name='cart_detail'), # This matches /shoppingcart/

    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('buy/<int:product_id>/', views.cash_on_delivery, name='cash_on_delivery'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]