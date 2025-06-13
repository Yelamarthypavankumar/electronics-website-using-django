from django.contrib import admin
from .models import Vendor, VendorProduct

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('name', 'user__username')

@admin.register(VendorProduct)
class VendorProductAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'product', 'stock')
    search_fields = ('vendor__name', 'product__name')
