from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from products.models import Product  # import Product model

def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # homepage shows products
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('vendors/', include('vendors.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('blog/', include('blog.urls')),
    path('shoppingcart/', include('shoppingcart.urls', namespace='shoppingcart')),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])


