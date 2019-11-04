from django.shortcuts import render, redirect
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cart.add(product,
                 form.cleaned_data['quantity'],
                 form.cleaned_data['update'])
    return redirect(product.get_absolute_url())


def cart_remove(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart:CartDetail')


def cart_detail(request):
    cart = Cart(request)
    print(cart.cart.values())
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(initial={
    #         'quantity': item['quantity'],
    #         'update': True
    #     })
    return render(request, 'cart/detail.html', {'cart': cart})