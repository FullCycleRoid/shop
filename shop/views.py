from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.context_processors import csrf
from shop.models import Category, Product
from cart.forms import CartAddProductForm

from cart.cart import Cart


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)
    return render(request, 'shop/product_list.html', {'categories': categories,
                                                      'products': products,
                                                      'category': category,
                                                      'cart':Cart(request)})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,  id=id, slug=slug,  available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form, 'cart':Cart(request)}
    context.update(csrf(request))
    return render_to_response('shop/product_detail.html', context)

