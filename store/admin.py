from django.contrib import admin
from .models import Product, Cart

admin.site.register(Product)
admin.site.register(Cart)
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Cart.objects.create(
        product=product,
        quantity=1
    )

    return redirect('home')